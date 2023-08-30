from fastapi import HTTPException, status


InvalidPassword = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect"
)
