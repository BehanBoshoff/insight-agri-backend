from sqlalchemy.orm import Session

from core.auth.hashing import Hasher
from core.schemas.user import UserCreate
from db.models.user import User


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
