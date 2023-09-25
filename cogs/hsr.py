import discord
from mihomo import Language, MihomoAPI
from mihomo.models import StarrailInfoParsed
from mihomo.errors import InvalidParams
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
        self.hsrapi = MihomoAPI(language=Language.EN)
        # ^^ Honkai: Star Rail API Client, used for getting HSR Information

    async def get_hsr_data(self, uid: int) -> StarrailInfoParsed | None:
        """Requests data from Honkai: Star Rail using a UID

        Args:
            uid (int): A user ID from Honkai: Star Rail. Ex: 613792348, 714028257

        Returns:
            StarrailInfoParsed | None: Returns the Honkai: Star Rail user information based on the UID if the data is retrievable. If not, returns None.
        """
        try: # Attempting to get the data
            data: StarrailInfoParsed = await self.hsrapi.fetch_user(uid, replace_icon_name_with_url=True)
            return data
        except InvalidParams: # If an invalid UID is passed
            return None

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
