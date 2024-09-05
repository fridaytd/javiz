import httpx
from javiz.services.lottery import get_newest_lottery_results
from javiz.utils.models import Interaction
from javiz.utils.logger import get_logger
from javiz.utils.constants import DISCORD_WEBHOOK_URL

logger = get_logger("background_task")


def lottery_background_task(
    interaction: Interaction,
) -> None:
    response = __send_follow_message(
        application_id=interaction.application_id,
        token=interaction.token,
        content=get_newest_lottery_results(),
    )
    logger.info(f"lottery background task webhooks status code: {response.status_code}")
    if response.status_code != 200:
        logger.info(response.json())


def __send_follow_message(
    application_id: str,
    token: str,
    content: str,
) -> httpx.Response:
    url = f"{DISCORD_WEBHOOK_URL}x/{application_id}/{token}"

    json = {
        "content": content,
    }

    return httpx.post(url, json=json)
