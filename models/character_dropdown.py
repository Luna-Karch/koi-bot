from discord.ui import Select
from mihomo.models import StarrailInfoParsed


class CharacterDropdown(Select):
    def __init__(self, user_id: int, hsr_info: StarrailInfoParsed):
        options = ...
        super().__init__(
            placeholder="Select a character",
            max_values=1,
            min_values=1,
            options=options,
        )
