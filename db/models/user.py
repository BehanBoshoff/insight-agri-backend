from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from .base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    pic = Column(String, nullable=True)
    fullname = Column(String, nullable=True)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    occupation = Column(String, nullable=True)
    company_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    communication = Column(Boolean, nullable=True)
    jobs = relationship("Job", back_populates="owner")
    address = relationship("Address", back_populates="user", uselist=False)
    social_networks = relationship(
        "SocialNetworks", back_populates="user", uselist=False
    )
