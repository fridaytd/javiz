from fastapi import APIRouter
from javiz.utils.deps import ValidateDep
from javiz.utils.enums import InterationType, InteractionCallbackType
from javiz.utils.models import Interaction, InteractionResponse, Message
from javiz.utils.logger import get_logger
from javiz.router.handler import command_handler, ping_handler

logger = get_logger("discord_router")

router = APIRouter(
    tags=["Discord"],
)


@router.post("/")
async def discord_webhook(
    _: ValidateDep,
    interaction: Interaction,
) -> InteractionResponse:
    logger.info(interaction.model_dump_json())

    match interaction.type:
        case InterationType.PING:
            return ping_handler()

        case InterationType.APPLICATION_COMMAND:
            return command_handler(
                interaction=interaction,
            )

    return InteractionResponse(
        type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=Message(content="Sorry! I don't understand"),
    )
