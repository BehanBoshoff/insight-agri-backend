from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base_class import Base


class Address(Base):
    id = Column(Integer, primary_key=True, index=True)
    addressLine = Column(String, nullable=True)
    city = Column(String, nullable=True)
    province = Column(String, nullable=True)
    postCode = Column(String, nullable=True)
    users = relationship("UserAddress", back_populates="address")
