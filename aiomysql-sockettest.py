import asyncio
import datetime
import logging

import aiomysql


async def test_async():
    conn = await aiomysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password='rootpw',
        db='mysql'
    )

    async with conn.cursor() as cur:
        pass
        #await cur.execute("select 1")
        #r = await cur.fetchone()
        #print(f"{r=}")

    conn.close()


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
