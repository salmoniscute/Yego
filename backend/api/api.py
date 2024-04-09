from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

from config import HOST, PORT

from .routers import (
    info_router,
    auth_router,
    component_router,
    course_router,
    course_bulletin_router,
    discussion_router,
    file_router,
    selected_course_router,
    user_router,
    website_bulletin_router
)

app = FastAPI()

app.include_router(info_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(course_router)
app.include_router(component_router)
app.include_router(selected_course_router)
app.include_router(file_router)
app.include_router(course_bulletin_router)
app.include_router(website_bulletin_router)
app.include_router(discussion_router)


origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def api_run():
    config = Config(
        app=app,
        host=HOST,
        port=PORT
    )
    server = Server(config=config)

    await server.serve()
