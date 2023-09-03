import os
import typing
import discord
from discord import app_commands
from discord.ext import commands


SETUP_KWARGS: dict[str, typing.Any] = {
    "intents": discord.Intents.all(),  # What the bot intends to use
    "command_prefix": "~",  # The command prefix
    "help_command": None,  # Removing the default help command
    "description": "A cute, general purpose discord bot",  # bot description
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


def cprint(text: str, rgb: tuple[int]) -> None:
    for color_value in rgb:
        if not (0 <= color_value <= 255):
            raise IndexError("Color value cannot exceed 255 or preceed 0")

    """Prints text in any color provided RGB values

    Args:
        text (str): The text you want to print in rgb
        rgb (tuple[int]): RGB format of the color value you want to print the text with

    Returns (None): Prints a statement
    
    Raises:
        IndexError: If the color values are outside the RGB spectrum, if any value is outside the range 0 <= r, g, b <= 255 
    """
    output_template: str = "\033[38;2;red;green;bluem{text}\033[0m"
    # ^^ Template string, replaces values red, green, blue, and text accordingly
    print(
        output_template.replace("red", str(rgb[0]))
        .replace("green", str(rgb[1]))
        .replace("blue", str(rgb[2]))
        .replace("{text}", text)
    )  # Printing the replace output


cprint("test", (255, 255, 255))


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
