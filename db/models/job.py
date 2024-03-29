from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base_class import Base


class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_posted = Column(Date)
    is_active = Column(Boolean(), default=True)
