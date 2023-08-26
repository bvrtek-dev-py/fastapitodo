from pydantic import BaseModel
from .auth import UserRead


class TaskBase(BaseModel):
    name: str
    description: str
    is_done: bool

    class Config:
        orm_mode = True


class TaskRead(TaskBase):
    id: int
    owner: UserRead

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    ...
