from fastapi import FastAPI

from todo.api_v1.config import Config
from todo.api_v1.routers.todo_router import router as todo_router
from todo.api_v1.database.config import engine, Base

app = FastAPI(title="Todo API",
              openapi_url=Config.API_VERSION_STRING+"/openapi.json",
              docs_url=Config.API_VERSION_STRING+"/docs",
              redoc_url=Config.API_VERSION_STRING+"/redoc",
              version="1.0.0")

# include api routes
app.include_router(todo_router)


# connect to database on start
@app.on_event('startup')
async def startup():
    Base.metadata.create_all(bind=engine)
