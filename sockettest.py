import asyncio
import sys

import aiomysql


loop = asyncio.new_event_loop()


async def test_example():
    conn = await aiomysql.connect(unix_socket=sys.argv[1], user='root', password='rootpw', db='mysql')

    async with conn.cursor() as cur:
        await cur.execute("select 1")
        r = await cur.fetchone()
        print(f"{r=}")

    conn.close()


loop.run_until_complete(test_example())
