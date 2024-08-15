import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from javiz.router import discord_router


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
    return {
        "message": "Hello from Javiz",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
