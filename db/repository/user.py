from sqlalchemy.orm import Session

from core.auth.hashing import Hasher
from core.schemas.user import UserCreate
from db.models.address import Address
from db.models.social_networks import SocialNetworks
from db.models.user import User


def create_new_user(user: UserCreate, db: Session):
    address = Address(
        addressLine=user.address.addressLine,
        city=user.address.city,
        province=user.address.province,
        postCode=user.address.postCode,
    )
    social_networks = SocialNetworks(
        linkedIn=user.social_networks.linkedIn,
        facebook=user.social_networks.facebook,
        twitter=user.social_networks.twitter,
        instagram=user.social_networks.instagram,
    )
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=user.is_superuser,
        pic=user.pic,
        fullname=user.fullname,
        firstname=user.firstname,
        lastname=user.lastname,
        occupation=user.occupation,
        company_name=user.company_name,
        phone=user.phone,
        communication=user.communication,
        address=address,
        social_networks=social_networks,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user
