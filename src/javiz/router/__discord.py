from fastapi import APIRouter
from javiz.utils.deps import ValidateDep
from javiz.utils.enums import InterationType
from javiz.utils.models import Interaction, InteractionResponse
from javiz.utils.logger import get_logger
from javiz.router.handler.command import command_handler
from javiz.router.handler.ping import ping_handler

logger = get_logger("discord_router")

router = APIRouter(
    tags=["Discord"],
)


@router.post("/")
async def discord_webhook(
    _: ValidateDep,
    interaction: Interaction,
) -> InteractionResponse | None:
    logger.info(interaction)

    match interaction.type:
        case InterationType.PING:
            return ping_handler()

        case InterationType.APPLICATION_COMMAND:
            return command_handler(interaction)
