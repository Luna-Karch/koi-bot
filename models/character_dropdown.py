import discord
from typing import Dict
from mihomo.models import StarrailInfoParsed


class CharacterDropdown(discord.ui.Select):
    def __init__(self, user_id: int, parsed_data):
        options = self.make_options(parsed_data)
        super().__init__(
            placeholder="Select a character",
            max_values=1,
            min_values=1,
            options=options,
        )

    def make_options(
        self, parsed_data: Dict[str, discord.Embed]
    ) -> list[discord.SelectOption]:
        """Converts the parsed data given into a list of discord select options to be added to the view

        Args:
            parsed_data (Dict[str, discord.Embed]): Information Retrieved from the Mihomo API and parsed by my parsing function in hsr.py

        Returns:
            list[discord.SelectOption]: A list of discord.SelectOption objects. Both the label and value attributes are set to the character name
        """
        options = [
            discord.SelectOption(label=character.name, value=character.name)
            for character in parsed_data["characters"]
        ]

        return options

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.followup.send(f"Your choice is {self.values[0]}")
