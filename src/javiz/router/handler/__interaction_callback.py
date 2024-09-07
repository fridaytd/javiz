import httpx

from javiz.utils.helper import get_interaction_callback_url
from javiz.utils.logger import get_logger
from javiz.utils.models import Interaction, InteractionResponse

logger = get_logger("interaction_callback")


def interaction_callback(
    interaction: Interaction,
    interaction_response: InteractionResponse,
) -> httpx.Response | None:
    res = httpx.post(
        url=get_interaction_callback_url(interaction.id, interaction.token),
        json=interaction_response.model_dump(mode="json"),
    )

    if res.status_code == 200 or res.status_code == 204:
        logger.info(res.status_code)
        return res

    else:
        logger.error(
            f"interaction callback get error. Status code:{res.status_code}. {res.content}"
        )
