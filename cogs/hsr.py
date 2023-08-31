import discord
from discord import app_commands
from discord.ext import commands


class HSR(commands.Cog):
    """
    Honkai: Star Rail Interaction Commands Cog
    Houses all commands relating to Honkai: Star Rail
    """

    def __init__(self, client: commands.Bot) -> None:
        self.client: commands.Bot = client
        # ^^ Sets the client to be an attribute of the class


async def setup(client: commands.Bot) -> None:
    """
    Cog Setup Function, required for every cog that needs to be loaded.
    Adds all the commands in the cog to the client and loads them
    """
    await client.add_cog(HSR(client))
