from fastapi import APIRouter
from app.endpoint import producer, user

router = APIRouter()
router.include_router(user.router)
router.include_router(producer.router)
