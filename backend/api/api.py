from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

from config import HOST, PORT

from .routers import (
    info_router,
    auth_router,
    course_router,
    course_bulletin_router,
    discussion_router,
    discussion_topic_router,
    discussion_topic_reply_router,
    file_router,
    notification_router,
    selected_course_router,
    subscription_router,
    user_router,
    website_bulletin_router,
    report_router,
    course_material_router,
    material_info_router,
    submitted_assignment_router,
    report_reply_router
)

app = FastAPI()

app.include_router(info_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(website_bulletin_router)
app.include_router(report_router)
app.include_router(report_reply_router)
app.include_router(course_router)
app.include_router(selected_course_router)
app.include_router(course_bulletin_router)
app.include_router(discussion_router)
app.include_router(discussion_topic_router)
app.include_router(discussion_topic_reply_router)
app.include_router(course_material_router)
app.include_router(material_info_router)
app.include_router(submitted_assignment_router)
app.include_router(file_router)
app.include_router(subscription_router)
app.include_router(notification_router)

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
