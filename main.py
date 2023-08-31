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

print(load_token())
