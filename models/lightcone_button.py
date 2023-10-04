import discord
from mihomo.models import StarrailInfoParsed


class LightconeButton(discord.ui.Button):
    def __init__(self):
        super().__init__(...)