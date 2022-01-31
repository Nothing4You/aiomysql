import asyncio
import datetime
import logging
import socket


def set_keep_alive(writer):
    transport = writer.transport
    transport.pause_reading()
    raw_sock = transport.get_extra_info('socket', default=None)
    raw_sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    transport.resume_reading()


def set_nodelay(writer, value):
    flag = int(bool(value))
    transport = writer.transport
    transport.pause_reading()
    raw_sock = transport.get_extra_info('socket', default=None)
    raw_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, flag)
    transport.resume_reading()


async def test_async():
    reader, writer = await asyncio.open_connection("127.0.0.1", 3306)

    set_keep_alive(writer)
    set_nodelay(writer, True)

    b = await reader.readexactly(1)
    print(f"read 1 byte: {b=}")
    writer.write(bytes(0))
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
