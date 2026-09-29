from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/cities", tags=["Cities"])

# ── Cloud Save Slots Endpoints ────────────────────────────────────────────────

@router.post("/save-slot", response_model=schemas.SaveSlotResponse, status_code=status.HTTP_200_OK)
def save_city_slot(data: schemas.SaveSlotRequest, db: Session = Depends(get_db)):
    """
    Save or overwrite a city in cloud save slot (0 to 4).
    Stores metadata + the complete CityState serialized JSON string.
    """
    existing = db.query(models.CitySave).filter(models.CitySave.slot_index == data.slot_index).first()

    if existing:
        existing.city_name = data.city_name
        existing.difficulty = data.difficulty
        existing.day = data.day
        existing.year = data.year
        existing.budget = data.budget
        existing.population = data.population
        existing.happiness = data.happiness
        existing.sustainability = data.sustainability
        existing.smart_city_score = data.smart_city_score
        existing.level = data.level
        existing.progression_title = data.progression_title
        existing.state_json = data.state_json
        db.commit()
        db.refresh(existing)
        return {
            "success": True,
            "slot_index": existing.slot_index,
            "city_name": existing.city_name,
            "message": f"City '{existing.city_name}' updated in cloud slot {existing.slot_index}",
            "updated_at": existing.updated_at
        }
    else:
        new_slot = models.CitySave(
            slot_index=data.slot_index,
            city_name=data.city_name,
            difficulty=data.difficulty,
            day=data.day,
            year=data.year,
            budget=data.budget,
            population=data.population,
            happiness=data.happiness,
            sustainability=data.sustainability,
            smart_city_score=data.smart_city_score,
            level=data.level,
            progression_title=data.progression_title,
            state_json=data.state_json
        )
        db.add(new_slot)
        db.commit()
        db.refresh(new_slot)
        return {
            "success": True,
            "slot_index": new_slot.slot_index,
            "city_name": new_slot.city_name,
            "message": f"City '{new_slot.city_name}' created in cloud slot {new_slot.slot_index}",
            "updated_at": new_slot.updated_at
        }

@router.get("/slots", response_model=list[schemas.SlotSummary])
def list_cloud_slots(db: Session = Depends(get_db)):
    """
    Returns summary metadata of all active cloud save slots.
    """
    return db.query(models.CitySave).order_by(models.CitySave.slot_index.asc()).all()

@router.get("/slots/{slot_index}", response_model=schemas.SlotDetail)
def get_cloud_slot(slot_index: int, db: Session = Depends(get_db)):
    """
    Retrieve the full city save state (including state_json) for a given slot.
    """
    slot = db.query(models.CitySave).filter(models.CitySave.slot_index == slot_index).first()
    if not slot:
        raise HTTPException(status_code=404, detail=f"Cloud save slot {slot_index} is empty")
    return slot

@router.delete("/slots/{slot_index}")
def delete_cloud_slot(slot_index: int, db: Session = Depends(get_db)):
    """
    Delete a cloud save slot.
    """
    slot = db.query(models.CitySave).filter(models.CitySave.slot_index == slot_index).first()
    if not slot:
        raise HTTPException(status_code=404, detail=f"Cloud save slot {slot_index} not found")
    db.delete(slot)
    db.commit()
    return {"success": True, "message": f"Cloud save slot {slot_index} deleted"}

# ── Simulation Telemetry Endpoints ────────────────────────────────────────────

@router.post("/telemetry", response_model=schemas.TelemetryOut, status_code=status.HTTP_201_CREATED)
def record_telemetry(data: schemas.TelemetryCreate, db: Session = Depends(get_db)):
    """
    Record periodic simulation telemetry point (economy, health, pollution, utilities).
    """
    parent = db.query(models.CitySave).filter(models.CitySave.slot_index == data.slot_index).first()
    if not parent:
        # Create a stub if slot not explicitly saved yet
        parent = models.CitySave(
            slot_index=data.slot_index,
            city_name=f"City Slot {data.slot_index}",
            budget=data.budget,
            population=data.population,
            happiness=data.happiness,
            sustainability=data.sustainability,
            state_json="{}"
        )
        db.add(parent)
        db.commit()
        db.refresh(parent)

    point = models.CityTelemetry(
        city_save_id=parent.id,
        slot_index=data.slot_index,
        in_game_day=data.in_game_day,
        in_game_year=data.in_game_year,
        budget=data.budget,
        population=data.population,
        happiness=data.happiness,
        sustainability=data.sustainability,
        traffic_efficiency=data.traffic_efficiency,
        pollution=data.pollution,
        crime_rate=data.crime_rate,
        power_balance=data.power_balance,
        water_balance=data.water_balance
    )
    db.add(point)
    db.commit()
    db.refresh(point)
    return point

@router.get("/telemetry/{slot_index}", response_model=list[schemas.TelemetryOut])
def get_slot_telemetry(slot_index: int, limit: int = 50, db: Session = Depends(get_db)):
    """
    Retrieve telemetry history for a given slot.
    """
    return db.query(models.CityTelemetry)\
             .filter(models.CityTelemetry.slot_index == slot_index)\
             .order_by(models.CityTelemetry.in_game_day.asc())\
             .limit(limit).all()

# ── Legacy Endpoints (Backward Compatibility) ──────────────────────────────────

@router.post("", response_model=schemas.CityCreateResponse, status_code=status.HTTP_201_CREATED)
def create_city(data: schemas.CityCreate, db: Session = Depends(get_db)):
    city = models.City(
        city_name=data.city_name,
        difficulty=data.difficulty,
        starting_budget=data.starting_budget,
        current_budget=data.starting_budget,
        population=1200,
        happiness=72,
        sustainability=68,
        smart_city_score=0
    )
    db.add(city)
    db.commit()
    db.refresh(city)
    return {"success": True, "city_id": city.id, "city_name": city.city_name}

@router.get("", response_model=list[schemas.CityOut])
def list_cities(db: Session = Depends(get_db)):
    return db.query(models.City).order_by(models.City.id.desc()).all()

@router.get("/{city_id}", response_model=schemas.CityOut)
def get_city(city_id: int, db: Session = Depends(get_db)):
    city = db.get(models.City, city_id)
    if not city:
        raise HTTPException(404, "City not found")
    return city

@router.put("/{city_id}", response_model=schemas.CityOut)
def update_city(city_id: int, data: schemas.CityUpdate, db: Session = Depends(get_db)):
    city = db.get(models.City, city_id)
    if not city:
        raise HTTPException(404, "City not found")
    for k, v in data.model_dump(exclude_none=True).items():
        setattr(city, k, v)
    db.commit()
    db.refresh(city)
    return city

@router.delete("/{city_id}")
def delete_city(city_id: int, db: Session = Depends(get_db)):
    city = db.get(models.City, city_id)
    if not city:
        raise HTTPException(404, "City not found")
    db.delete(city)
    db.commit()
    return {"success": True, "deleted_city_id": city_id}
