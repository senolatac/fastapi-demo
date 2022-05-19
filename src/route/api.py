from fastapi import APIRouter
from src.endpoint import producer, user

router = APIRouter()
router.include_router(user.router)
router.include_router(producer.router)
