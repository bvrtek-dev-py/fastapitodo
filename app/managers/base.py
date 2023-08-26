from sqlalchemy.orm import Session


class BaseManager:
    def __init__(self, session: Session):
        self._session = session

    def delete(self, obj) -> None:
        self._session.delete(obj)
        self._session.commit()
