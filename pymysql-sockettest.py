import sys

import pymysql


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


test_sync()
