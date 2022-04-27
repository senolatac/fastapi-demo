from fastapi import APIRouter
from src.models.message import ExampleModel
import src.queue.producer as producer

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/producer",
    tags=["Producer"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    task = ExampleModel(task_id='123', description='test')
    await producer.send_rabbitmq(task)
    return {"message": f"Task {task.task_id} added"}
