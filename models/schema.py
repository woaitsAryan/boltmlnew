from pydantic import BaseModel, EmailStr, Field

class DayInput(BaseModel):
    text: str

class RegisterModel(BaseModel):
    name: str
    password: str = Field(..., min_length=8)
    email: EmailStr

class LoginModel(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    
class TokenData(BaseModel):
    user_id: str | None = None