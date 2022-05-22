import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi import Query
from sqlalchemy.orm import Session

from app import schema
from app.dependency.database import get_db
from app.model.user import UserModel
from typing import Optional

# APIRouter creates path operations for user module
from app.security.role_checker import RoleChecker
from app.security.security_config import USER
from app.service.user_service import get_user, get_all_users, get_user_by_id, insert_user, get_user_by_email

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


@router.get("/dummy/{user_id}", dependencies=[Depends(allow_create_resource)])
async def read_user(user_id: int):
    logging.info("Read user request with %s", user_id)
    return {"id": user_id, "full_name": "Danny Manny", "email": "danny.manny@gmail.com"}


@router.get("/db/{user_id}", dependencies=[Depends(allow_create_resource)])
async def read_user_from_db(user_id: int, db: Session = Depends(get_db)):
    logging.info("Read user request with %s", user_id)
    db_user = get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/db/email/{email}", dependencies=[Depends(allow_create_resource)])
async def read_user_from_db_by_email(email: str, db: Session = Depends(get_db)):
    logging.info("Read user request with %s", email)
    db_user = get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/all-users-from-db", dependencies=[Depends(allow_create_resource)])
async def read_users_from_db(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logging.info("Read all user")
    return get_all_users(db, skip=skip, limit=limit)


@router.get("/placeholder/{user_id}")
async def read_user_json_placeholder(user_id: int):
    logging.info("Read user-placeholder request with %s", user_id)
    return get_user(user_id)


@router.get("/detail")
async def read_users(q: Optional[str] = Query(None, max_length=50)):
    results = {"users": [{"id": 1}, {"id": 2}]}
    if q:
        results.update({"q": q})
    return results


@router.post("/add")
async def add_user(user: UserModel):
    return {"user": user.username, "is_active": True}


@router.post("/db/add")
async def add_user_to_db(user: schema.user.CreateUser, db: Session = Depends(get_db)):
    return insert_user(db, user=user)


@router.put("/update")
async def update_user(user: UserModel):
    return {"id": user.user_id, "user": user.username, "email": user.email}


@router.delete("/{user_id}/delete")
async def delete_user(user_id: int):
    return {"id": user_id, "is_deleted": True}
