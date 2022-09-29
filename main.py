from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.config import settings
# from api.v1.general_pages.route_homepage import general_pages_router
from db.session import engine
from db.base import Base


def include_router(app):
    # app.include_router(general_pages_router)
    print("...")


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

