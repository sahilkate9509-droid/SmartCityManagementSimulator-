import hashlib
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/auth", tags=["Authentication"])

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

@router.post("/register", response_model=schemas.AuthResponse, status_code=status.HTTP_201_CREATED)
def register_user(data: schemas.UserRegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new Mayor or Admin account for Smart City Management.
    """
    existing_user = db.query(models.User).filter(
        (models.User.username == data.username) | (models.User.email == data.email)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered."
        )

    new_user = models.User(
        username=data.username.strip(),
        email=data.email.strip().lower(),
        full_name=data.full_name.strip(),
        role=data.role,
        department=data.department,
        password_hash=hash_password(data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "success": True,
        "message": f"Welcome Mayor {new_user.full_name}! Account created successfully.",
        "user": new_user,
        "token": f"token_{new_user.id}_{new_user.username}"
    }

@router.post("/login", response_model=schemas.AuthResponse)
def login_user(data: schemas.UserLoginRequest, db: Session = Depends(get_db)):
    """
    Authenticate an existing Mayor / Admin user.
    """
    identifier = data.username_or_email.strip()
    user = db.query(models.User).filter(
        (models.User.username == identifier) | (models.User.email == identifier.lower())
    ).first()

    # Default fallback for initial demo if DB is clean
    if not user and (identifier == "admin@smartcity.gov" or identifier == "admin"):
        if data.password == "admin123" or data.password == "admin":
            return {
                "success": True,
                "message": "Default Admin logged in successfully.",
                "user": schemas.UserOut(
                    id=1,
                    username="admin",
                    email="admin@smartcity.gov",
                    full_name="Chief Administrator",
                    role="Chief Mayor & Urban Planner",
                    department="Executive Planning"
                ),
                "token": "admin_master_token"
            }

    if not user or user.password_hash != hash_password(data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please check your username/email and password."
        )

    return {
        "success": True,
        "message": f"Welcome back, Mayor {user.full_name}!",
        "user": user,
        "token": f"token_{user.id}_{user.username}"
    }

@router.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    """
    List all registered mayor/admin profiles.
    """
    return db.query(models.User).order_by(models.User.id.desc()).all()
