from fastapi import APIRouter, Depends, status, exceptions
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth.jwt_token import Token
from backend.session import get_db
from backend.hashing import Hash
from schemas import auth
from managers import user


router = APIRouter(tags=["Auth"])


@router.post(
    "/create/", response_model=auth.UserRead, status_code=status.HTTP_201_CREATED
)
def create_user(request: auth.UserCreate, session: Session = Depends(get_db)):
    manager = user.UserManager(session)
    return manager.create_user(request)


@router.post(
    "/login/",
)
def login(
    request: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)
):
    manager = user.UserManager(session)
    searched_user = manager.get_user_by_email(request.username)
    if searched_user is None:
        raise exceptions.HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if not Hash.verify(request.password, searched_user.password):
        raise exceptions.HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Password is incorrect"
        )
    access_token = Token.create_access_token(data={"sub": searched_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
