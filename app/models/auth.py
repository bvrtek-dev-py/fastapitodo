from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.orm import relationship

from backend.session import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String(255), unique=True)
    password = Column(String(255))
    first_name = Column(String(255), default="")
    last_name = Column(String(255), default="")
    date_of_birth = Column(Date)
    id = Column(Integer, index=True, primary_key=True)

    tasks = relationship("Task", back_populates="owner")
