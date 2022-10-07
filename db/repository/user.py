from typing import List

from sqlalchemy.orm import Session

from .address import get_addresses
from .address import get_base_address
from core.auth.hashing import Hasher
from core.schemas.user import ShowUser
from core.schemas.user import UserCreate
from db.models.address import Address
from db.models.user import User
from db.models.user_address import UserAddress


def create_new_user(user_create: UserCreate, db: Session):
    blank_address: Address = get_base_address(db)
    user_address = UserAddress()
    if blank_address:
        user_address.address = blank_address
    else:
        user_address.address = Address(
            addressLine="", city="", province="", postCode=""
        )

    user = User(
        username=user_create.username,
        email=user_create.email,
        hashed_password=Hasher.get_password_hash(user_create.password),
        is_active=True,
        is_superuser=user_create.is_superuser,
        pic=user_create.pic,
        fullname=user_create.fullname,
        firstname=user_create.firstname,
        lastname=user_create.lastname,
        occupation=user_create.occupation,
        company_name=user_create.company_name,
        phone=user_create.phone,
        communication=user_create.communication,
    )
    user.addresses.append(user_address)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user
