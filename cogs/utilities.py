import base64
import discord
from discord import app_commands
from discord.ext import commands

blue = 0x73BCF8  # Hex color blue stored for embed usage


class Utilities(commands.Cog):
    """
    Utilites Commands Cog
    Houses all utility commands for the discord bot
    """

    def __init__(self, client: commands.Bot) -> None:
        self.client: commands.Bot = client
        # ^^ Sets the client to be an attribute of the class

    @app_commands.command(name="base64-encode", description="Encodes a given text")
    @app_commands.describe(text="The text to excode to base64")
    async def base64_encode(self, interaction: discord.Interaction, text: str) -> None:
        """
        Takes an input text and converts it to base64 format before
        sending it as a discord embed

        Args:
            interaction (discord.Interaction): Provided automatically by discord, the interaction data from the command
            text (str): Text provided by the command user, to convert to base64

        Returns (None): sends a discord embed as a result and returns nothing
        """

        await interaction.response.defer(ephemeral=True)  # Wait ephemerally
        embed = discord.Embed(color=blue, title="✅ Base64 Encoded Result")
        # ^^ Create the embed with it's constructor
        text_as_bytes: bytes = base64.b64encode(bytes(text, "utf-8"))
        # ^^ Convert text to base64 bytes
        embed.description = f"```\n{text_as_bytes.decode()}\n```"
        # ^^ Set embed description to text format of base64 bytes
        embed.set_footer(
            text="Requested by @" + interaction.user.name,
            icon_url=interaction.user.avatar.url if interaction.user.avatar else "",
        )
        # ^^ Set the embed footer to the one who used to command
        await interaction.followup.send(embed=embed)  # Send the resulting embed

    @app_commands.command(
        name="base64-decode",
        description="Decodes a given base64 string into plain text",
    )
    @app_commands.describe(text="The base64 text to decode to plain text")
    async def base64_decode(self, interaction: discord.Interaction, text: str) -> None:
        """
        Takes a base64 input as a string text and attempts to convert it
        back into plain text.

        Args:
            interaction (discord.Interaction): Provided by discord, the interaction which called the command
            text (str): The input text, should be given in base64 format

        Returns (None): Sends a discord embed as a result and returns nothing
        """

        await interaction.response.defer(ephemeral=True)  # Waits ephemerally
        embed = discord.Embed(color=blue, title="✅ Base64 Decoded Result")
        # ^^ Create the embed with it's constructor
        try:  # Attempt to convert the base64 input to plain text
            embed.description = f"```\n{str(base64.b64decode(text))[2:-1]}\n```"
            """ ^^ Adds the converted plain text to the embed description
            and converts it in one line.
            If this throws base64.binascii.Error
            An invalid input was given
            """
        except base64.binascii.Error:  # In the case that an invalid input was given
            embed.description = f"```diff\n- Text was not in base64 format\n```"
            # ^^ Change the embed description to reflect that

        embed.set_footer(
            text="Requested by @" + interaction.user.name,
            icon_url=interaction.user.avatar.url if interaction.user.avatar else "",
        )
        # ^^ Set the embed footer to reflect the user who called the interaction

        await interaction.followup.send(embed=embed)  # Send the resulting embed


async def setup(client: commands.Bot) -> None:
    """
    Cog Setup Function, required for every cog that needs to be loaded.
    Adds all the commands in the cog to the client and loads them
    """
    await client.add_cog(Utilities(client))
