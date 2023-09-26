from discord.ui import View
from models.character_dropdown import CharacterDropdown
from mihomo.models import StarrailInfoParsed


class PlayerCardView(View):
    def __init__(self, user_id: int, hsr_info: StarrailInfoParsed):
        self.user_id = user_id
        self.hsr_info = hsr_info
        super().__init__(timeout=None)
        self.add_item(CharacterDropdown(user_id, hsr_info))
