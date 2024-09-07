import httpx

from javiz.utils.logger import get_logger
from javiz.utils.helper import get_follow_message_url
from javiz.utils.models import Interaction


logger = get_logger("follow message")


def follow_message(
    interaction: Interaction,
    message: str,
) -> httpx.Response | None:
    res = httpx.post(
        url=get_follow_message_url(
            application_id=interaction.application_id, token=interaction.token
        ),
        json={"content": message},
    )

    if res.status_code / 100 == 2:
        logger.info(res.status_code)
        return res

    else:
        logger.error(
            f"interaction callback get error. Status code:{res.status_code}. {res.content}"
        )
