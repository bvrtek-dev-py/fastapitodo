from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .jwt_token import Token
from sqlalchemy.orm import Session
from managers.user import UserManager
from backend.session import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_active_user(
    token: str = Depends(oauth2_scheme), session: Session = Depends(get_db)
):
    token_data = Token.verify_token(token)
    return UserManager(session).get_user_by_email(token_data.email)
