from sqlalchemy import Column, String, Text, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from backend.session import Base


class Task(Base):
    __tablename__ = "tasks"

    name = Column(String(255))
    description = Column(Text(2000))
    is_done = Column(Boolean, default=False)
    id = Column(Integer, primary_key=True, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="tasks")
