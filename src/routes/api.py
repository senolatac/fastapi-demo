from fastapi import APIRouter
from src.endpoints import user, producer

router = APIRouter()
router.include_router(user.router)
router.include_router(producer.router)
