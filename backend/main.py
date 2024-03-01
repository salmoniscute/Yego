from asyncio import run

from api import api_run


async def main():
    await api_run()

if __name__ == "__main__":
    run(main=main())
