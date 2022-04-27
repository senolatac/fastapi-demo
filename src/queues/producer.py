import os
import json
from aio_pika import connect, Message

async def send_rabbitmq(msg = {}):
    connection = await connect(os.getenv('EXAMPLE_QUEUE', "amqp://guest:guest@localhost/guest"))

    channel = await connection.channel()

    await channel.default_exchange.publish(
        Message(json.dumps(msg.dict()).encode("utf-8")),
        routing_key = os.getenv('EXAMPLE_QUEUE', "fastapi_task")
    )

    await connection.close()
