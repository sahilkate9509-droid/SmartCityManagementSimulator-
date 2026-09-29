from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr

# ── User & Authentication Schemas ─────────────────────────────────────────────
class UserRegisterRequest(BaseModel):
    username: str = Field(min_length=3, max_length=80)
    email: str = Field(min_length=5, max_length=120)
    password: str = Field(min_length=4, max_length=100)
    full_name: str = Field(min_length=2, max_length=120)
    role: str = "City Mayor"
    department: str = "Executive Planning"

class UserLoginRequest(BaseModel):
    username_or_email: str = Field(min_length=3, max_length=120)
    password: str = Field(min_length=4, max_length=100)

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: str
    full_name: str
    role: str
    department: str
    created_at: datetime | None = None

class AuthResponse(BaseModel):
    success: bool = True
    message: str
    user: UserOut | None = None
    token: str | None = None

# ── Legacy City Schemas (Backward Compatibility) ──────────────────────────────
class CityCreate(BaseModel):
    city_name: str = Field(min_length=2, max_length=120)
    difficulty: str = "Easy"
    starting_budget: float = Field(gt=0)

class CityUpdate(BaseModel):
    city_name: str | None = None
    difficulty: str | None = None
    current_budget: float | None = None
    population: int | None = None
    happiness: float | None = None
    sustainability: float | None = None
    smart_city_score: float | None = None

class CityOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    city_name: str
    difficulty: str
    starting_budget: float
    current_budget: float
    population: int
    happiness: float
    sustainability: float
    smart_city_score: float

class CityCreateResponse(BaseModel):
    success: bool = True
    city_id: int
    city_name: str

# ── Cloud Save Slot Schemas ───────────────────────────────────────────────────
class SaveSlotRequest(BaseModel):
    slot_index: int = Field(ge=0, le=4, description="Save slot index (0 to 4)")
    city_name: str = Field(min_length=1, max_length=120)
    difficulty: str = "Easy"
    day: int = 1
    year: int = 2026
    budget: float = 150000.0
    population: int = 120
    happiness: float = 55.0
    sustainability: float = 30.0
    smart_city_score: float = 0.0
    level: int = 1
    progression_title: str = "Small Town"
    state_json: str = Field(description="Complete serialized CityState JSON string")

class SaveSlotResponse(BaseModel):
    success: bool = True
    slot_index: int
    city_name: str
    message: str = "City saved to cloud successfully"
    updated_at: datetime | None = None

class SlotSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    slot_index: int
    city_name: str
    difficulty: str
    day: int
    year: int
    budget: float
    population: int
    happiness: float
    sustainability: float
    smart_city_score: float
    level: int
    progression_title: str
    updated_at: datetime | None = None

class SlotDetail(SlotSummary):
    state_json: str

# ── Simulation Telemetry Schemas ──────────────────────────────────────────────
class TelemetryCreate(BaseModel):
    slot_index: int = Field(ge=0, le=4)
    in_game_day: int
    in_game_year: int = 2026
    budget: float
    population: int
    happiness: float
    sustainability: float
    traffic_efficiency: float = 60.0
    pollution: float = 15.0
    crime_rate: float = 28.0
    power_balance: float = 0.0
    water_balance: float = 0.0

class TelemetryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    slot_index: int
    in_game_day: int
    in_game_year: int
    budget: float
    population: int
    happiness: float
    sustainability: float
    traffic_efficiency: float
    pollution: float
    crime_rate: float
    power_balance: float
    water_balance: float
    timestamp: datetime | None = None

# ── Health & Status Schemas ───────────────────────────────────────────────────
class DatabaseStatus(BaseModel):
    engine: str
    connected: bool
    url_masked: str

class SystemHealthResponse(BaseModel):
    status: str = "online"
    service: str = "Smart City Management Simulator API"
    version: str = "1.0.0"
    database: DatabaseStatus
    active_cloud_saves: int
