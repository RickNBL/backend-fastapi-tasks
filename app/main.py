from fastapi import FastAPI
from .database import Base, engine
from .routes import users, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "API rodando 🚀"}