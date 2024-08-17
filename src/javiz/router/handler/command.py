from javiz.utils.models import (
    Interaction,
    ApplicationCommandData,
    InteractionResponse,
    Message,
)
from javiz.utils.enums import InteractionCallbackType
from javiz.services.lottery import get_newest_lottery_results


def command_handler(
    interaction: Interaction,
) -> InteractionResponse:
    data = ApplicationCommandData.model_validate(interaction.data)
    match data.name:
        case "hello":
            return hello_command()

        case "lottery":
            return lottery_command()

    return InteractionResponse(
        type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=Message(content="Can not find the command"),
    )


def hello_command() -> InteractionResponse:
    return InteractionResponse(
        type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=Message(content="Hello! From Javiz with love"),
    )


def lottery_command() -> InteractionResponse:
    lottery_results = get_newest_lottery_results()
    return InteractionResponse(
        type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=Message(content=lottery_results),
    )
