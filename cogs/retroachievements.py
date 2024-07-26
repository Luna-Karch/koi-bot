import ast
import json
import discord
import subprocess
from datetime import datetime
from discord.ext import commands
from discord import app_commands

blue = 0x73BCF8  # Hex color blue stored for embed usage

class Retroachievements(commands.Cog):
    """Contains all commands related to retroachievements"""
    def __init__(self, client: commands.Bot):
        self.client: commands.Bot  = client

    @app_commands.command(name = "retro-profile", description = "get a users profile from retroachievements if it exists") 
    @app_commands.describe(username = "The retroachievements username of the person you want to lookup")
    async def retro_profile(self, interaction: discord.Interaction, username: str):
        # Runs a script in js to fetch the user data and captures it's stdout to display
        await interaction.response.defer()

        stdout = subprocess.check_output(f"node cogs/retroachievements-js/getUserProfile.mjs {username}", shell = True)
        modified_stdout: str = stdout.decode("utf-8")
        dict_stdout: dict = json.loads(modified_stdout)

        profile_picture_url: str = "https://media.retroachievements.org" + dict_stdout.get("userPic")
        member_since_as_datetime: datetime = datetime.strptime(dict_stdout.get("memberSince"), "%Y-%m-%d %H:%M:%S")

        output_embed: discord.Embed = discord.Embed(color = blue, title = "Retro Profile for " + dict_stdout.get("user"), description = "")
        output_embed.set_thumbnail(url = profile_picture_url)
        output_embed.set_footer(text = f"Member since {member_since_as_datetime.strftime('%B %d, %Y')}")
        output_embed.description += f"-# {dict_stdout.get('richPresenceMsg')}\n"
        output_embed.description += f"**__{dict_stdout.get('totalPoints')}__ ({dict_stdout.get('totalTruePoints')})** total points.\n"

        # TODO: get game from dict_stdout.get("lastGameId") and find a nice way to display it

        await interaction.followup.send(embed = output_embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Retroachievements(client))
