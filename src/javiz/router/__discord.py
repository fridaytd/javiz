from fastapi import APIRouter
from javiz.utils.deps import ValidateDep

router = APIRouter(
    # prefix="/discord",
    tags=["Discord"],
)


@router.post("/")
def discord_webhook(
    request: ValidateDep,
):
    print(request)
    if request["type"] == 1:
        return {
            "type": 1,
            "data": {},
        }

    return {"message": "hihi"}
