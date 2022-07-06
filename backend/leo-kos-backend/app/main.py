from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.routers import trips, root, users
from core.config import settings

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(trips.router,prefix='/trips')
    _app.include_router(users.router,prefix='/auth')

    return _app


app = get_application()
