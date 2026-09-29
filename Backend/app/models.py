from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    full_name = Column(String(120), nullable=False)
    role = Column(String(60), nullable=False, default="City Mayor")
    department = Column(String(80), nullable=False, default="Executive Planning")
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String(120), nullable=False, index=True)
    difficulty = Column(String(20), nullable=False, default="Easy")
    starting_budget = Column(Float, nullable=False)
    current_budget = Column(Float, nullable=False)
    population = Column(Integer, nullable=False, default=0)
    happiness = Column(Float, nullable=False, default=70.0)
    sustainability = Column(Float, nullable=False, default=60.0)
    smart_city_score = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class CitySave(Base):
    """
    Cloud Save Slot model for Smart City Management Simulator.
    Stores complete simulation snapshots (including 3D building counts, utilities,
    financials, technology unlocks, and event states) serialized as state_json.
    """
    __tablename__ = "city_saves"

    id = Column(Integer, primary_key=True, index=True)
    slot_index = Column(Integer, nullable=False, unique=True, index=True) # 0 to 4
    city_name = Column(String(120), nullable=False, index=True)
    difficulty = Column(String(30), nullable=False, default="Easy")
    day = Column(Integer, nullable=False, default=1)
    year = Column(Integer, nullable=False, default=2026)
    budget = Column(Float, nullable=False, default=150000.0)
    population = Column(Integer, nullable=False, default=120)
    happiness = Column(Float, nullable=False, default=55.0)
    sustainability = Column(Float, nullable=False, default=30.0)
    smart_city_score = Column(Float, nullable=False, default=0.0)
    level = Column(Integer, nullable=False, default=1)
    progression_title = Column(String(60), nullable=False, default="Small Town")
    
    # Complete CityState serialized JSON
    state_json = Column(Text, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    telemetry = relationship("CityTelemetry", back_populates="city_save", cascade="all, delete-orphan")

class CityTelemetry(Base):
    """
    Time-series simulation telemetry for tracking historical performance,
    generating economy charts, and auditing city health over time.
    """
    __tablename__ = "city_telemetry"

    id = Column(Integer, primary_key=True, index=True)
    city_save_id = Column(Integer, ForeignKey("city_saves.id", ondelete="CASCADE"), nullable=False, index=True)
    slot_index = Column(Integer, nullable=False, index=True)
    in_game_day = Column(Integer, nullable=False)
    in_game_year = Column(Integer, nullable=False)
    budget = Column(Float, nullable=False)
    population = Column(Integer, nullable=False)
    happiness = Column(Float, nullable=False)
    sustainability = Column(Float, nullable=False)
    traffic_efficiency = Column(Float, default=60.0)
    pollution = Column(Float, default=15.0)
    crime_rate = Column(Float, default=28.0)
    power_balance = Column(Float, default=0.0)
    water_balance = Column(Float, default=0.0)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    city_save = relationship("CitySave", back_populates="telemetry")
