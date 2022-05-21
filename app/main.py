import asyncio
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.route.api import router as api_router
import app.queue.listener as listener
from app.core.config import get_app_settings


def get_application() -> FastAPI:
    settings = get_app_settings()

    app = FastAPI(**settings.fastapi_kwargs)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    return app


app = get_application()


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(listener.consume(loop))
