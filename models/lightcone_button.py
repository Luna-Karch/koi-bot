import discord
import typing
from mihomo.models import StarrailInfoParsed


class LightconeButton(discord.ui.Button):
    def __init__(
        self,
        user_id: int,
        parsed_data: typing.Dict[str, discord.Embed]
        | typing.Dict[str, typing.Dict[str, discord.Embed]],
    ):
        super().__init__(...)
