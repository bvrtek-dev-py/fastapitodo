from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return password_context.hash(password)

    @staticmethod
    def verify(raw_password: str, hashed_password: str):
        return password_context.verify(raw_password, hashed_password)
