import discord
from discord import app_commands
from discord.ext import commands

class HSR(commands.Cog):
    """
    Honkai: Star Rail Interaction Commands Cog
    Houses all commands relating to Honkai: Star Rail
    """
    def __init__(self, client: commands.Bot):
        self.client: commands.Bot = client


async def setup(client: commands.Bot):
    """
    Cog Setup Function, required for every cog that needs to be loaded.
    Adds all the commands in the cog to the client and loads them
    """
    await client.add_cog(HSR(client))
