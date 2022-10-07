from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

from .base_class import Base


class UserAddress(Base):
    user_id = Column("user_id", ForeignKey("user.id"), primary_key=True)
    address_id = Column("address_id", ForeignKey("address.id"), primary_key=True)
    user = relationship("User", back_populates="addresses")
    address = relationship("Address", back_populates="users")
