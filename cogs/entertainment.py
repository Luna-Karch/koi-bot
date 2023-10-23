import discord
import asyncio
import requests
from discord import app_commands
from discord.ext import commands


class Entertainment(commands.Cog):
    """Holds all entertainment commands that exsist entirely for fun and don't have a more specific purpose"""

    def __init__(self, client: commands.Bot) -> None:
        self.client: commands.Bot = client

    def get_hug_gif(self):
        hug_api_url = "https://api.otakugifs.xyz/gif?reaction=hug"
        data = requests.get(hug_api_url)
        return data.json().get("url")

    @app_commands.command(name="hug", description="Give a user of your choice a hug")
    @app_commands.describe(user="The user you want to give a hug to")
    async def _hug(self, interaction: discord.Interaction, user: discord.Member):
        await interaction.response.defer()

        active_event_loop = asyncio.get_running_loop()
        api_results = await active_event_loop.run_in_executor(None, self.get_hug_gif)

        hug_embed = discord.Embed(title="Hugs!", color = 0x1d83a5)
        hug_embed.description = (
            f"*{interaction.user.name} is giving {user.name} a hug!*"
        )
        hug_embed.set_image(url=api_results)

        await interaction.followup.send(user.mention, embed=hug_embed)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Entertainment(client))
