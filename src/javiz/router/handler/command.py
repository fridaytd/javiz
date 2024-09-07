from javiz.utils.models import (
    Interaction,
    ApplicationCommandData,
    InteractionResponse,
    Message,
)
from javiz.utils.enums import InteractionCallbackType


from javiz.services.lottery import get_newest_lottery_results
from .__interaction_callback import interaction_callback
from .__follow_message import follow_message


def command_handler(
    interaction: Interaction,
) -> InteractionResponse:
    data = ApplicationCommandData.model_validate(interaction.data)
    match data.name:
        case "hello":
            return hello_command()

        case "lottery":
            return lottery_command(interaction=interaction)

    return InteractionResponse(
        type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=Message(content="Can not find the command"),
    )


def hello_command() -> InteractionResponse:
    return InteractionResponse(
        type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=Message(content="Hello! From Javiz with love"),
    )


def lottery_command(
    interaction: Interaction,
) -> InteractionResponse:
    interaction_callback(
        interaction=interaction,
        interaction_response=InteractionResponse(
            type=InteractionCallbackType.DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE
        ),
    )
    follow_message(
        interaction=interaction,
        message=get_newest_lottery_results(),
    )
    return InteractionResponse(
        type=InteractionCallbackType.PONG,
    )
