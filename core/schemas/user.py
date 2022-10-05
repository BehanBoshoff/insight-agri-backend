from typing import List

from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    pic: str
    fullname: str
    firstname: str
    lastname: str
    language: str
    time_zone: str
    roles: List[int]
    occupation: str
    company_name: str
    phone: str
    address: str
    social_networks: str
    communication: bool


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    pic: str = None
    fullname: str = None
    firstname: str = None
    lastname: str = None
    language: str = None
    time_zone: str = None
    roles: List[int] = None
    occupation: str = None
    company_name: str = None
    phone: str = None
    address: str = None
    social_networks: str = None
    communication: bool = None

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
