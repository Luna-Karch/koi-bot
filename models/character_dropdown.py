import discord
from mihomo.models import StarrailInfoParsed


class CharacterDropdown(discord.ui.Select):
    def __init__(self, user_id: int, hsr_info: StarrailInfoParsed):
        options = ...
        super().__init__(
            placeholder="Select a character",
            max_values=1,
            min_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.followup.send(f"Your choice is {self.values[0]}")
