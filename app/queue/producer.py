import json
from aio_pika import connect, Message

from app.core.config import get_app_settings

SETTINGS = get_app_settings()


async def send_rabbitmq(msg={}):
    connection = await connect(SETTINGS.rabbit_host)

    channel = await connection.channel()

    await channel.default_exchange.publish(
        Message(json.dumps(msg.dict()).encode("utf-8")),
        routing_key=SETTINGS.rabbit_example_queue
    )

    await connection.close()
