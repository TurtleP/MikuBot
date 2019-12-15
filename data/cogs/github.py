import json
import re
from urllib import request

import discord
from discord.ext import commands
from discord.ext.commands import Cog

from data.utility import is_developer


class GitHub(Cog):
    def __init__(self, bot):
        self.bot = bot

    def generate_binary_embed(self, release_type, binaries):
        embed = discord.Embed(title=f"{release_type} Binaries")

        for key, value in binaries.items():
            real_name = " ".join(
                re.search(r"(Nintendo)-(\w+)", key).group(1, 2))
            embed.add_field(name=real_name, value=f"[Download]({value})")

        return embed

    def get_release_information(self):
        repository_request = request.Request(
            "https://api.github.com/repos/TurtleP/LovePotion/releases")
        repository_request.add_header("user-agent", "PotionBot/1.0")

        releases = list()

        with request.urlopen(repository_request) as response:
            json_bytes = response.read()
            releases = json.loads(json_bytes.decode("utf-8"))

        if len(releases) > 0:
            return releases[0]["assets"]


    # TODO: re-use some of this code for the nightly builds
    @commands.guild_only()
    @commands.command(name='release', aliases=['stability'])
    async def release(self, ctx, console=None):
        """Posts the stable release binaries."""
        releases = self.get_release_information()

        binaries = dict()
        for item in releases:
            binaries[item["name"]] = item["browser_download_url"]

        remove_key = False
        if console is not None:
            for key in binaries:
                if not console.lower() in key.lower():
                   remove_key = True
                   break

        if remove_key:
            del binaries[key]

        embed = self.generate_binary_embed("Stable™", binaries)

        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command(name='nightly')
    async def nightly(self, ctx, console=None):
        """Posts the nightly binaries."""
        pass

    @commands.guild_only()
    @commands.command(name='issue_search')
    async def issue_search(self, ctx, criteria):
        """Search the repository Issues for <criteria>."""
        pass


def setup(bot):
    bot.add_cog(GitHub(bot))
