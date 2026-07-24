from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

# create application/backend server. Every endpoint belongs to this
app = FastAPI()


class RegisterUser(BaseModel):
    email: EmailStr
    password: str

# return python dictionary--> which is converted to JSON automatically.
# will check other services as added


@app.get("/health")
def healthCheck():
    return {
        "Status": "Healthy"
    }


@app.post("/register")
def registerUser(user: RegisterUser):
    return {
        "Message": "User Registration Successful!",
        "Email": user.email
    }





