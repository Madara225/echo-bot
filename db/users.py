import aiosqlite
import os


class DataBase:
    async def create_db(self) -> None:
        connect = await aiosqlite.connect(os.path.join(
            "db", "users.db"
        ))

        async with connect.cursor() as cursor:
            await cursor.execute(
                """
                    CREATE TABLE users(
                        user INT PRIMARY KEY
                    );
                """
            )

        await cursor.close()
        await connect.close()

    
    async def add_user(self, user_id: int) -> None:
        connect = await aiosqlite.connect(os.path.join(
            "db", "users.db"
        ))

        async with connect.cursor() as cursor:
            await cursor.execute(
                """
                    INSERT OR IGNORE INTO users(user) VALUES(?);
                """,
                (user_id,)
            )
            
            await connect.commit()

        await cursor.close()
        await connect.close()

    
    async def get_users(self) -> list:
        connect = await aiosqlite.connect(os.path.join(
            "db", "users.db"
        ))

        async with connect.cursor() as cursor:
            await cursor.execute("SELECT * FROM users;")
            data = await cursor.fetchall()

        await cursor.close()
        await cursor.close()

        return [x[0] for x in data]