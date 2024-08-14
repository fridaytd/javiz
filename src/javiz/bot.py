import os

import discord
from typing import Final
from javiz.utils.logger import get_logger

logger = get_logger(__name__)

TOKEN: Final = os.getenv("DISCORD_TOKEN", "")


intents = discord.Intents()

client = discord.Client(
    intents=intents,
)


@client.event
async def on_ready():
    logger.info(f"{client.user} has connected to Discord!")


client.run(
    token=TOKEN,
)
