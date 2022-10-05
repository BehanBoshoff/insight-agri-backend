import logging

from fastapi import FastAPI
from fastapi.logger import logger
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from api.base import api_router
from db.base import Base
from db.config import settings
from db.session import engine


def include_router(app):
    app.include_router(api_router)


def configure_static(app):
    # app.mount("/static", StaticFiles(directory="static"), name="static")
    print("...")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    origins = [
        "http://localhost",
        "http://localhost:4200",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    gunicorn_logger = logging.getLogger("gunicorn.error")
    logger.handlers = gunicorn_logger.handlers
    if __name__ != "main":
        logger.setLevel(gunicorn_logger.level)
    else:
        logger.setLevel(logging.DEBUG)

    include_router(app)
    configure_static(app)
    create_tables()  # new
    return app


app = start_application()
