import asyncio
import datetime
import logging


async def test_async():
    reader, writer = await asyncio.open_connection("127.0.0.1", 3306)
    b = await reader.readexactly(1)
    print(f"read 1 byte: {b=}")
    writer.close()
    await writer.wait_closed()


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)8s - %(name)s:%(funcName)s - %(message)s",
)

logging.Formatter.formatTime = (
    lambda self, record, datefmt: datetime.datetime.fromtimestamp(
        record.created, datetime.timezone.utc
    )
    .astimezone()
    .isoformat()
)

asyncio.run(test_async(), debug=True)
