import discord
from discord.ext import commands
from discord import app_commands

class Retroachievements(commands.Cog):
    """Contains all commands related to retroachievements"""
    def __init__(self, client: commands.Bot):
        self.client: commands.Bot  = client

   @app_commands.command(name = "retro-profile", description = "get a users profile from retroachievements if it exists") 
   @app_commands.describe(username = "The retroachievements username of the person you want to lookup")
   async def retro_profile(self, interaction: discord.Interaction, username: str):
       await interaction.response.send_message("This is a placeholder command!")

async def setup(client: commands.Bot) -> None:
    client.add_cog(Retroachievements(client))
