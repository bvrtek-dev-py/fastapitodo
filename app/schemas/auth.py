from datetime import date
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    first_name: str = None
    last_name: str = None
    date_of_birth: date = None


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
