from asyncio import run

from api import api_run
from database.mysql import close_db, init_db

async def main():
    await init_db()
    await api_run()
    await close_db()


if __name__ == "__main__":
    run(main=main())
