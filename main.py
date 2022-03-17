# developer = Duco

import asyncio
from websockets import serve
import mysql.connector

async def handle_conn(websocket):
    while True:
        try:
            message = await websocket.recv()
            (name, score, gamename) = message.split(",")
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO {gamename} (name,score) VALUES (\"{name}\",{score});")
            db.commit()
        except:
            pass

async def main():
    async with serve(handle_conn, "0.0.0.0", 7777):
        await asyncio.Future()

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root_passwd",
        database="highscores"
        )

asyncio.run(main())
