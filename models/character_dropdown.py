import discord
from mihomo.models import StarrailInfoParsed


class CharacterDropdown(discord.ui.Select):
    def __init__(self, user_id: int, hsr_info: StarrailInfoParsed):
        options = self.make_options(hsr_info)
        super().__init__(
            placeholder="Select a character",
            max_values=1,
            min_values=1,
            options=options,
        )

    def make_options(self, hsr_info: StarrailInfoParsed) -> list[discord.SelectOption]:
        """Converts the StarrailInfoParsed data given into a list of discord select options to be added to the view

        Args:
            hsr_info (StarrailInfoParsed): Information Retrieved from the Mihomo API

        Returns:
            list[discord.SelectOption]: A list of discord.SelectOption objects. Both the label and value attributes are set to the character name
        """
        options = [
            discord.SelectOption(label=character.name, value=character.name)
            for character in hsr_info.characters
        ]

        return options

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.followup.send(f"Your choice is {self.values[0]}")
