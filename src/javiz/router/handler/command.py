from javiz.utils.models import (
    Interaction,
    ApplicationCommandData,
    InteractionResponse,
    Message,
)
from javiz.utils.enums import InteractionCallbackType


def command_handler(
    interaction: Interaction,
) -> InteractionResponse:
    data = ApplicationCommandData.model_validate(interaction.data)
    match data.name:
        case "hello":
            return hello_command()

    return InteractionResponse(
        type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=Message(content="Can not find the command"),
    )


def hello_command() -> InteractionResponse:
    return InteractionResponse(
        type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=Message(content="Hello! From Javiz with love"),
    )
