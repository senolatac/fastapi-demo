import logging

from fastapi import APIRouter, Depends
from fastapi import Query
from src.model.user import UserModel
from typing import Optional

# APIRouter creates path operations for user module
from src.security.role_checker import RoleChecker
from src.security.security_config import USER

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

allow_create_resource = RoleChecker([USER])


@router.get("/")
async def read_root():
    return [{"id": 1}, {"id": 2}]


@router.get("/{user_id}", dependencies=[Depends(allow_create_resource)])
async def read_user(user_id: int):
    logging.info("Read user request with %s", user_id)
    return {"id": user_id, "full_name": "Danny Manny", "email": "danny.manny@gmail.com"}


@router.get("/detail")
async def read_users(q: Optional[str] = Query(None, max_length=50)):
    results = {"users": [{"id": 1}, {"id": 2}]}
    if q:
        results.update({"q": q})
    return results


@router.post("/add")
async def add_user(user: UserModel):
    return {"user": user.username, "is_active": True}


@router.put("/update")
async def update_user(user: UserModel):
    return {"id": user.user_id, "user": user.username, "email": user.email}


@router.delete("/{user_id}/delete")
async def delete_user(user_id: int):
    return {"id": user_id, "is_deleted": True}
