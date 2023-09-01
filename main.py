import os
import typing
import discord
from discord import app_commands
from discord.ext import commands


SETUP_KWARGS: dict[str, typing.Any] = {
    "intents": discord.Intents.all(),
    "command_prefix": "~",
    "help_command": None,
    "description": "A cute, general purpose discord bot",
}  # Bot setup keyword arguments


def load_token() -> str:
    """
    Loads the bot's authorization token from the token file
    Args: None
    Returns (str): The bot's authorization token
    """
    with open("token.txt", "r", encoding="utf-8") as f:
        token: str = f.read()

    return token.strip()


def blue(text: str) -> None:
    """
    Prints the given text in blue in the terminal
    """
    print(f"\033[38;2;115;188;248m{text}\033[0m")


async def load_cogs(client: commands.Bot) -> None:
    """
    Loads all the cogs from the cogs folder
    and connects them to the discord bot

    Args:
        client (commands.Bot): The discord bot object

    Returns (None): There is nothing to return
    """

    for filename in os.listdir("cogs"):  # for every cog in the cogs folder
        if filename[-1] == "y":
            # ^^ If the cog ends in "y", checking if it's a python file
            await client.load_extension(f"cogs.{filename[:-3]}")
            # ^^ Load the cog into the bot
