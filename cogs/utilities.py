import base64
import discord
from discord import app_commands
from discord.ext import commands


class Utilities(commands.Cog):
    """
    Utilites Commands Cog
    Houses all utility commands for the discord bot
    """

    def __init__(self, client: commands.Bot) -> None:
        self.client: commands.Bot = client
        # ^^ Sets the client to be an attribute of the class


async def setup(client: commands.Bot) -> None:
    """
    Cog Setup Function, required for every cog that needs to be loaded.
    Adds all the commands in the cog to the client and loads them
    """
    await client.add_cog(Utilities(client))
