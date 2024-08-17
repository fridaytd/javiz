from pydantic import BaseModel

from javiz.utils.enums import (
    InterationType,
    InteractionContextType,
    ApplicationCommandTypes,
    InteractionCallbackType,
)


class InteractionData(BaseModel):
    pass


class ApplicationCommandData(InteractionData):
    id: str
    name: str
    type: ApplicationCommandTypes
    resolved: dict | None = None
    options: list | None = None
    guild_id: str | None = None
    target_id: str | None = None


class MessageComponentData(InteractionData):
    custom_id: str
    component_type: int  # Note: Change to Enum in the future
    values: list | None = None
    resolved: dict | None = None


class ModalSubmitData(InteractionData):
    custom_id: str
    component_: list  # Note: Change to list of message components in the future


class Interaction(BaseModel):
    id: str
    application_id: str
    type: InterationType
    data: dict | None = None  # Note: take a look in the future
    guild: dict | None = None
    guild_id: str | None = None
    channel: dict | None = None
    channel_id: str | None = None
    member: dict | None = None
    user: dict | None = None
    token: str
    version: int
    message: dict | None = None
    app_permissions: str
    locale: str | None = None
    guild_locale: str | None = None
    entitlements: list
    authorizing_integration_owners: dict
    context: InteractionContextType | None = None


class InteractionCallbackData(BaseModel):
    pass


class Message(InteractionCallbackData):
    tts: bool | None = None
    content: str | None = None
    embeds: list | None = None  # Note: Update in the future
    allowed_mentions: dict | None = None  # Note: Update in the future
    flags: int | None = None  # Note: Update in the future
    components: list | None = None  # Note: Update in the future
    attachments: list | None = None  # Note: Update in the future
    poll: dict | None = None  # Note: Update in the future


class Autocomplete(InteractionCallbackData):
    choices: list  # Note: Update in the future change to a list of choices


class Modal(InteractionCallbackData):
    custom_id: str
    title: str
    components: list  # Note: change to a list of components


class InteractionResponse(BaseModel):
    type: InteractionCallbackType
    data: Message | Autocomplete | Modal | None = None
