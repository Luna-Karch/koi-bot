import discord
from discord.ext import commands

class RetroGameInfoView(discord.ui.View):
    def __init__(self, dict_game_info_and_progress_stdout: dict, timeout = None):
        self.dict_game_info_and_progress_stdout = dict_game_info_and_progress_stdout
        super().__init__(timeout = timeout)

    @discord.ui.button(label = "More Game Information", style=discord.ButtonStyle.blurple)
    async def callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        print(self.dict_game_info_and_progress_stdout)
        # TODO: display game information nicely in an embed that gets sent upon clicking the button

        # Disable button after click
        button.disabled = True
        await interaction.response.edit_message(view = self)

