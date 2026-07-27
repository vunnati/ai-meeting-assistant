import bcrypt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from app.database import SessionLocal, engine, Base
from app.models import User

Base.metadata.create_all(bind = engine)

# create application/backend server. Every endpoint belongs to this
app = FastAPI()


class RegisterUser(BaseModel):
    email: EmailStr
    password: str


@app.get("/health")
def healthCheck():
    return {
        "Status": "Healthy"
    }


@app.post("/register")
def registerUser(user: RegisterUser):
    # open database session
    database = SessionLocal()

    existing_user = database.scalar(
        select(User).where(User.email == user.email)
    )
    
    password = user.password
    password_to_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()

    # raise HTTP error if user exists in db, else create new user entry
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email is already registered. Please Login."
        )
    else:
        new_user = User(
            email = user.email,
            hashed_password = bcrypt.hashpw(password_to_bytes, salt)
        )

    # add new user to database
    database.add(new_user)
    database.commit()
    database.refresh(new_user)

    # function return
    return{
        "message": "User successfully registered.",
    }