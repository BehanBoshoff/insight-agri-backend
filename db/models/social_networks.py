from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base_class import Base


class SocialNetworks(Base):
    id = Column(Integer, primary_key=True, index=True)
    linkedIn = Column(String, unique=False, nullable=True)
    facebook = Column(String, unique=False, nullable=True)
    twitter = Column(String, unique=False, nullable=True)
    instagram = Column(String, unique=False, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="social_networks")
