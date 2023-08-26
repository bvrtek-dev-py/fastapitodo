from .base import BaseManager
from models.task import Task
from models.auth import User
from schemas.task import TaskCreate


class TaskManager(BaseManager):
    def create_task(self, data: TaskCreate, user: User):
        task = Task(**data.model_dump(), owner=user)
        self._session.add(task)
        self._session.commit()
        self._session.refresh(task)
        return task

    def get_tasks(self) -> list[Task]:
        return self._session.query(Task).all()

    def get_task(self, task_id: int) -> Task:
        return self._session.query(Task).filter(Task.id == task_id).first()

    def update_task(self, data: TaskCreate, obj: Task) -> Task:
        for key, value in data.model_dump().items():
            setattr(obj, key, value) if value else None
        self._session.commit()
        self._session.refresh(obj)
        return obj
