import asyncio


async def test_async():
    reader, writer = await asyncio.open_connection("127.0.0.1", 3306)
    b = await reader.readexactly(1)
    print(f"read 1 byte: {b=}")
    writer.close()
    await writer.wait_closed()


loop = asyncio.new_event_loop()
loop.run_until_complete(test_async())
