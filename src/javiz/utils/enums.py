from enum import Enum


class InterationType(Enum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5


class InteractionContextType(Enum):
    GUILD = 0
    BOT_DM = 1
    PRIVATE_CHANNEL = 2


class ApplicationCommandTypes(Enum):
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3


class InteractionCallbackType(Enum):
    PONG = 1  # 	ACK a Ping
    CHANNEL_MESSAGE_WITH_SOURCE = 4  # respond to an interaction with a message
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = (
        5  # ACK an interaction and edit a response later, the user sees a loading state
    )
    DEFERRED_UPDATE_MESSAGE = 6  # for components, ACK an interaction and edit the original message later; the user does not see a loading state
    UPDATE_MESSAGE = 7  # for components, edit the message the component was attached to
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = (
        8  # respond to an autocomplete interaction with suggested choices
    )
    MODAL = 9  # respond to an interaction with a popup modal
    PREMIUM_REQUIRED = 10  # Deprecated; respond to an interaction with an upgrade button, only available for apps with monetization enabled
