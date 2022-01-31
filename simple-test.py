import asyncio


async def test_async():
    reader, writer = await asyncio.open_connection("127.0.0.1", 22)
    await reader.readexactly(1)
    print("read 1 byte")
    writer.close()
    await writer.wait_closed()


loop = asyncio.new_event_loop()
loop.run_until_complete(test_async())
