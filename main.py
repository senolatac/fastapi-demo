import asyncio
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.route.api import router as api_router
import src.queue.listener as listener

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(listener.consume(loop))
