from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from .address import AddressBase


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    pic: Optional[str]
    fullname: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    occupation: Optional[str]
    company_name: Optional[str]
    phone: Optional[str]
    communication: Optional[bool]


class ShowUser(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    pic: Optional[str]
    fullname: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    occupation: Optional[str]
    company_name: Optional[str]
    phone: Optional[str]
    # addresses: List[AddressBase]
    communication: Optional[bool]

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
