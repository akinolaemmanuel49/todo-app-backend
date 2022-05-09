from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError


from todo.api_v1.config import Config
from todo.api_v1.routers.todo_router import router as todo_router
from todo.api_v1.routers.user_router import router as user_router
from todo.api_v1.database.config import engine, Base
from todo.api_v1.utils.error_handler import validation_exception_handler


app = FastAPI(title="Todo API",
              openapi_url=Config.API_VERSION_STRING+"/openapi.json",
              docs_url=Config.API_VERSION_STRING+"/docs",
              redoc_url=Config.API_VERSION_STRING+"/redoc",
              version="1.0.0")


origins = [
    "*",
]


# middlerware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)


# include api routes
app.include_router(todo_router)
app.include_router(user_router)


# connect to database on start
@ app.on_event('startup')
async def startup():
    Base.metadata.create_all(bind=engine)
