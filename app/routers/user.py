from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.session import get_db
from auth.oauth2 import get_active_user
from schemas import auth
from managers.user import UserManager
from models.auth import User
from exceptions.user import UserNotFound


router = APIRouter(prefix="/user", tags=["User"])


@router.get("/list/", response_model=list[auth.UserRead])
def user_list(
    session: Session = Depends(get_db), current_user: User = Depends(get_active_user)
):
    manager = UserManager(session)
    return manager.get_users()


@router.get("/detail/{user_id}/", response_model=auth.UserRead)
def user_detail(
    user_id: int,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_active_user),
):
    manager = UserManager(session)
    user = manager.get_user(user_id)
    if user is None:
        raise UserNotFound
    return user
