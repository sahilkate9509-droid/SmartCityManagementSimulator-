import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

logger = logging.getLogger("smartcity.database")
logging.basicConfig(level=logging.INFO)

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()

# Normalize postgres:// to postgresql:// for SQLAlchemy 2.0
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

is_vercel = os.getenv("VERCEL") == "1"
DEFAULT_SQLITE = "sqlite:////tmp/smartcity.db" if is_vercel else "sqlite:///./smartcity.db"

# Default to SQLite if DATABASE_URL is empty
if not DATABASE_URL:
    DATABASE_URL = DEFAULT_SQLITE

DB_TYPE = "sqlite" if DATABASE_URL.startswith("sqlite") else "postgresql"

def create_db_engine(url: str):
    if url.startswith("sqlite"):
        logger.info(f"[Database] Using local SQLite database: {url}")
        return create_engine(
            url,
            connect_args={"check_same_thread": False},
            echo=False
        )
    else:
        logger.info(f"[Database] Connecting to PostgreSQL at {url.split('@')[-1] if '@' in url else 'cloud host'}")
        return create_engine(
            url,
            pool_size=10,
            max_overflow=20,
            pool_recycle=1800,
            pool_pre_ping=True,
            echo=False
        )

# Try connecting to the configured database, fallback to SQLite if PostgreSQL is unreachable
try:
    engine = create_db_engine(DATABASE_URL)
    with engine.connect() as conn:
        logger.info(f"[Database] Successfully connected to {DB_TYPE.upper()} database.")
except Exception as ex:
    logger.warning(f"[Database] Failed to connect to {DATABASE_URL}. Fallback to local SQLite. Error: {ex}")
    DATABASE_URL = DEFAULT_SQLITE
    DB_TYPE = "sqlite"
    engine = create_db_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)
    logger.info(f"[Database] Tables initialized successfully on {DB_TYPE.upper()}.")

def get_db_info() -> dict:
    return {
        "engine": DB_TYPE,
        "connected": True,
        "url_masked": DATABASE_URL.split("@")[-1] if "@" in DATABASE_URL else DATABASE_URL
    }
