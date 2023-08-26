from fastapi.exceptions import HTTPException
from fastapi import status


TaskNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
)


UserIsNotOwner = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="User is not owner of selected task"
)
