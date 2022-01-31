import asyncio
import sys

import pymysql
import aiomysql


def test_sync():
    conn = pymysql.connect(
        user="root",
        password="rootpw",
        unix_socket=sys.argv[1],
        db='mysql',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )

    with conn.cursor() as cur:
        cur.execute("select 1")
        r = cur.fetchone()
        print(f"{r=}")

    conn.close()


async def test_async():
    conn = await aiomysql.connect(
        unix_socket=sys.argv[1],
        user='root',
        password='rootpw',
        db='mysql'
    )

    async with conn.cursor() as cur:
        await cur.execute("select 1")
        r = await cur.fetchone()
        print(f"{r=}")

    conn.close()


test_sync()

loop = asyncio.new_event_loop()
loop.run_until_complete(test_async())
