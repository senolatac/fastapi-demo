import asyncio
from aio_pika import connect, IncomingMessage
import json
import os


async def on_message(message: IncomingMessage):
    txt = message.body.decode("utf-8")
    print(json.loads(txt))


async def consume(loop):
    connection = await connect(os.getenv('RABBIT_URL', "amqp://guest:guest@localhost/guest"), loop = loop)

    channel = await connection.channel()

    queue = await channel.declare_queue(os.getenv('EXAMPLE_QUEUE', "fastapi_task"), durable=True)

    await queue.consume(on_message, no_ack = True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(consume(loop))
    loop.run_forever()
    print('started')
