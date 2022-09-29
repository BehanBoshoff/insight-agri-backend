from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

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
    include_router(app)
    configure_static(app)
    create_tables()  # new
    return app


app = start_application()
