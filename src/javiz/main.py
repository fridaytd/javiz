from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from javiz.router import discord_router
from javiz.utils.logger import get_logger

logger = get_logger("main")


app: FastAPI = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(discord_router)


@app.get("/")
def hello():
    logger.info("Home page")
    return {
        "message": "Hello from Javiz",
    }


if __name__ == "__main__":
    try:
        import uvicorn

        uvicorn.run("main:app", reload=True)
    except Exception:
        pass
