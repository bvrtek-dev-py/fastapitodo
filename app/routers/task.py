from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from backend.session import get_db
from auth.oauth2 import get_active_user
from schemas.task import TaskRead, TaskCreate
from managers.task import TaskManager
from models.auth import User
from exceptions.task import TaskNotFound, UserIsNotOwner


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/list/", response_model=list[TaskRead])
def task_list(
    session: Session = Depends(get_db), current_user: User = Depends(get_active_user)
):
    return TaskManager(session).get_tasks()


@router.get("/detail/{task_id}/", response_model=TaskRead)
def task_detail(
    item_id: int,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_active_user),
):
    return TaskManager(session).get_task(item_id)


@router.post("/create/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    request: TaskCreate,
    session: Session = Depends(get_db),
    user: User = Depends(get_active_user),
):
    return TaskManager(session).create_task(request, user)


@router.put("/update/{task_id}/", response_model=TaskRead)
def update_task(
    task_id: int,
    request: TaskCreate,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_active_user),
):
    manager = TaskManager(session)
    task = manager.get_task(task_id)
    if task.owner != current_user:
        raise UserIsNotOwner
    return manager.update_task(request, task)


@router.delete("/delete/{task_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_active_user),
):
    manager = TaskManager(session)
    task = manager.get_task(task_id)
    if task.owner != current_user:
        raise UserIsNotOwner
    manager.delete(task)
    return "deleted"
