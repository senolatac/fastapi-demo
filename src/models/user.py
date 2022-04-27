from pydantic import BaseModel, Field
from typing import Optional

class UserModel(BaseModel):
    user_id: Optional[int] = None
    username: str
    email: str
    password: str
