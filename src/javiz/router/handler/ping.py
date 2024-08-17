from javiz.utils.models import InteractionResponse
from javiz.utils.enums import InteractionCallbackType


def ping_handler():
    return InteractionResponse(
        type=InteractionCallbackType.PONG,
    )
