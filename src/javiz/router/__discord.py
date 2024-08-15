from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/discord",
    tags=["Discord"],
)


@router.post("/")
def discord_webhook(request: Request):
    return {
        "type": 1,
        "data": {},
    }
