from datetime import timedelta, datetime

from jose import jwt, JWTError

from backend.settings import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
from .exceptions import CredentialsException
from schemas.jwt_token import TokenData


class Token:
    algorithm: str = ALGORITHM
    secret_key: str = SECRET_KEY
    token_expire: timedelta = ACCESS_TOKEN_EXPIRE_MINUTES

    @classmethod
    def create_access_token(cls, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(cls.token_expire)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, cls.secret_key, algorithm=cls.algorithm)
        return encoded_jwt

    @classmethod
    def verify_token(cls, token: str):
        try:
            payload = jwt.decode(token, key=cls.secret_key, algorithms=[cls.algorithm])
            email = payload.get("sub")
            if email is None:
                raise CredentialsException
            token_data = TokenData(email=email)
        except JWTError:
            raise CredentialsException
        return token_data
