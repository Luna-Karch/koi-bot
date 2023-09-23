import discord
from mihomo import Language, MihomoAPI
from mihomo.models import StarrailInfoParsed
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


    @app_commands.command(name = "hsr", description="Get information about a Honkai: Star Rail player from their UID")
    @app_commands.describe(uid = "The Honkai: Star Rail UID of the user you want the information on")
    async def hsr(self, interaction: discord.Interaction, uid: int):
        ...


async def setup(client: commands.Bot) -> None:
    """
    Cog Setup Function, required for every cog that needs to be loaded.
    Adds all the commands in the cog to the client and loads them
    """
    await client.add_cog(HSR(client))
