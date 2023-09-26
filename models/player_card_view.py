import discord
from typing import Dict
from models.character_dropdown import CharacterDropdown
from mihomo.models import StarrailInfoParsed


class PlayerCardView(discord.ui.View):
    def __init__(self, user_id: int, parsed_data: Dict[str, discord.Embed]):
        self.user_id = user_id
        self.parsed_data = parsed_data
        super().__init__(timeout=None)
        self.add_item(CharacterDropdown(user_id, parsed_data))
