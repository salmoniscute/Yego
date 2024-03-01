import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from api.router import router as default_router

app  = FastAPI()
app.include_router(default_router)


if __name__ == "__main__":
    load_dotenv("./settings/.env")
    uvicorn.run(app="main:app", host="0.0.0.0", port=int(os.getenv("PORT")), reload=bool(os.getenv("RELOAD")) )
