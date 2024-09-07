from .constants import DISCORD_WEBHOOK_URL


def get_interaction_callback_url(
    interaction_id: str,
    token: str,
) -> str:
    return f"https://discord.com/api/v10/interactions/{interaction_id}/{token}/callback"


def get_follow_message_url(
    application_id: str,
    token: str,
) -> str:
    return f"{DISCORD_WEBHOOK_URL}/{application_id}/{token}"
