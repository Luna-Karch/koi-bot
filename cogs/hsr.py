import discord
import typing
from typing import Dict
from random import choice
from discord import app_commands
from discord.ext import commands
from mihomo import Language, MihomoAPI
from mihomo.models import StarrailInfoParsed
from models.player_card_view import PlayerCardView
from mihomo.errors import InvalidParams, UserNotFound, HttpRequestError


class HSR(commands.Cog):
    """
    Honkai: Star Rail Interaction Commands Cog
    Houses all commands relating to Honkai: Star Rail
    """

    def __init__(self, client: commands.Bot) -> None:
        self.client: commands.Bot = client
        # ^^ Sets the client to be an attribute of the class
        self.hsrapi = MihomoAPI(language=Language.EN)
        # ^^ Honkai: Star Rail API Client, used for getting HSR Information
        self.FIVE_STAR_HEX = 0xFFAA4A
        self.FOUR_STAR_HEX = 0x8278ED
        self.ERROR_HEX = 0xFF5733
        # ^^ Constant variables used multiple times in the class

    async def get_hsr_data(
        self, uid: int
    ) -> StarrailInfoParsed | typing.Literal["Net"] | None:
        """Requests data from Honkai: Star Rail using a UID

        Args:
            uid (int): A user ID from Honkai: Star Rail. Ex: 613792348, 714028257

        Returns:
            StarrailInfoParsed | typing.Literal["Net"] | None:
              Returns the Honkai: Star Rail user information based on the UID if the data is retrievable.
              If there is an HttpRequestError, returns "Net"
              If there is another type of error, returns None
        """
        try:  # Attempting to get the data
            data: StarrailInfoParsed = await self.hsrapi.fetch_user(
                uid, replace_icon_name_with_url=True
            )
            return data
        except HttpRequestError:
            return "Net"
        except (InvalidParams, UserNotFound):  # If an invalid UID is passed
            return None

    def make_player_card(self, hsr_info: StarrailInfoParsed) -> discord.Embed:
        """Takes in a StarrailInfoParsed object and creates a discord Embed representing the player card.
        The player card refers to some general useful information about the player.

        This information includes Trailblaze Level, Friend Count, Equilibrium Level, Achievement Count,
        Amount of Characters Owned, and Amount of Light Cones Owned.

        Once the embed is created, returns it.

        Args:
            hsr_info (StarrailInfoParsed): The information retrieved from Mihomo's API

        Returns:
            discord.Embed: The player card embed
        """
        player_card_color = choice((self.FIVE_STAR_HEX, self.FOUR_STAR_HEX))
        player_card = discord.Embed(
            color=player_card_color,
            description="```",
        )
        player_card.set_author(
            name=hsr_info.player.name + " | " + str(hsr_info.player.uid),
            icon_url=hsr_info.player.avatar.icon,
        )

        player_attribute_mapping = {
            "Trailblaze Level": hsr_info.player.level,
            "Friends": hsr_info.player.friend_count,
            "Equilibrium Level": hsr_info.player.world_level,
            "Achievements": hsr_info.player.achievements,
            "Characters Owned": hsr_info.player.characters,
            "Light Cones Owned": hsr_info.player.light_cones,
        }

        for descriptor, value in player_attribute_mapping.items():
            player_card.description += f"{descriptor:17} -> {value:4d}\n"

        player_card.description += "```"

        return player_card

    def make_character_list(self, hsr_info: StarrailInfoParsed) -> discord.Embed:
        """Takes the hsr_info from the API and returns a list of the characters on the users profile

        Args:
            hsr_info (StarrailInfoParsed): The data from the Mihomo API

        Returns:
            discord.Embed: A discord embed whose title is a list of the characters the user has on their profile.
            To access it, simply access the embed's title property. Ex: character_list.title
        """
        character_list = discord.Embed(title="")
        character_list.title = ", ".join(
            character.name for character in hsr_info.characters
        )
        return character_list

    def make_character_cards(
        self, hsr_info: StarrailInfoParsed
    ) -> Dict[str, discord.Embed]:
        """Creates a dictionary of character names mapped to character cards, which are discord Embeds
        Each card will contain important information about each character

        Args:
            hsr_info (StarrailInfoParsed): Parsed Honkai: Star Rail Info parsed from Mihomo's API

        Returns:
            Dict[str, discord.Embed]: {character_name (str): character_card (discord.Embed)}
        """
        ...

    def parse_data(
        self, hsr_info: StarrailInfoParsed
    ) -> typing.Dict[str, discord.Embed]:
        player_card = self.make_player_card(hsr_info)
        character_list = self.make_character_list(hsr_info)

        resulting_dictionary = {
            "player_card": player_card,
            "characters": character_list,
        }
        return resulting_dictionary

    @app_commands.command(
        name="hsr",
        description="Get information about a Honkai: Star Rail player from their UID",
    )
    @app_commands.describe(
        uid="The Honkai: Star Rail UID of the user you want the information on"
    )
    async def hsr(self, interaction: discord.Interaction, uid: int):
        await interaction.response.defer()  # Bypass the 3 second timeout since this function requires an api call
        data = await self.get_hsr_data(uid)

        if isinstance(data, str):  # If an HttpRequestError occurs
            embed: discord.Embed = discord.Embed(
                color=self.ERROR_HEX,
                title="Whoops!",
                description="Something is wrong with the API service right now. It must be down for an update or something of the sort",
            )
            await interaction.followup.send(embed=embed)
            return  # Quitting the function early

        if data == None:  # If the request failed due to invalid parameters
            embed: discord.Embed = discord.Embed(
                color=self.ERROR_HEX,
                title="Whoops!",
                description="Either you provided an invalid input number or the user could not be found in the database.",
            )
            await interaction.followup.send(embed=embed)
            return  # Quitting the function early

        parsed_data = self.parse_data(data)  # Parsing the retrieved data

        await interaction.followup.send(
            embed=parsed_data["player_card"],
            view=PlayerCardView(interaction.user.id, parsed_data),
        )  # For now, just send the player card


async def setup(client: commands.Bot) -> None:
    """Cog Setup Function, required for every cog that needs to be loaded.
    Adds all the commands in the cog to the client and loads them"""
    await client.add_cog(HSR(client))
