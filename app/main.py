from fastapi import FastAPI
from routers import user, auth, task
from backend.session import Base, engine
from models import auth as auth_models, task as task_models


auth_models.Base.metadata.create_all(bind=engine)
task_models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(task.router)
