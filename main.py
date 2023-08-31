import discord
from discord import app_commands
from discord.ext import commands

def load_token() -> str:
    """
    Loads the bot's authorization token from the token file
    Args: None
    Returns (str): The bot's authorization token
    """
    with open("token.txt", "r", encoding = "utf-8") as f:
        token = f.read()

    return token.strip()

def blue(text: str) -> None:
    """
    Prints the given text in blue in the terminal
    """
    print(f"\033[38;2;115;188;248m{text}\033[0m")

blue("Hello World!")
