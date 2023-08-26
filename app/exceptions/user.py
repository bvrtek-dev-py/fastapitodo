from fastapi.exceptions import HTTPException
from fastapi import status


UserNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
)
