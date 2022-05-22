import requests
from sqlalchemy.orm import Session


from app.model import user_db
from app.schema.user import CreateUser


def get_user(user_id: int):
    url = "https://jsonplaceholder.typicode.com/users/{id}".format(id=user_id)

    response = requests.get(url)

    if response.ok:
        return response.json()
    else:
        return None


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_db.User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(user_db.User).filter(user_db.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(user_db.User).filter(user_db.User.email == email).first()


def insert_user(db: Session, user: CreateUser):
    db_user = user_db.User(email=user.email, name=user.name, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
