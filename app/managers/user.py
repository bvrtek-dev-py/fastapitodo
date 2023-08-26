from schemas import auth
from .base import BaseManager
from backend.hashing import Hash
from models.auth import User


class UserManager(BaseManager):
    def get_user_by_email(self, email: str) -> User | None:
        return self._session.query(User).filter(User.email == email).first()

    def get_users(self) -> list[User]:
        return self._session.query(User).all()

    def get_user(self, id: int) -> User | None:
        return self._session.query(User).filter(User.id == id).first()

    def create_user(self, request: auth.UserCreate) -> User:
        request.password = Hash.bcrypt(request.password)
        user = User(**request.model_dump())
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)
        return user
