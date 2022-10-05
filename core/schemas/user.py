from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from .address import AddressBase
from .social_networks import SocialNetworksBase


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
    address: AddressBase
    social_networks: SocialNetworksBase
    communication: Optional[bool]


class ShowUser(BaseModel):
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
    address: AddressBase
    social_networks: SocialNetworksBase
    communication: Optional[bool]

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
