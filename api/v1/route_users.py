from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.schemas.user import ShowUser
from core.schemas.user import UserCreate
from db.repository.user import create_new_user
from db.session import get_db

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
