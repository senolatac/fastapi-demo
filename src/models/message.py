from pydantic import BaseModel

class ExampleModel(BaseModel):
    task_id: str
    description: str
