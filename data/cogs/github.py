from urllib import request

import discord
from discord.ext import commands
from discord.ext.commands import Cog

from data.utility import is_developer


class GitHub(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name='release', aliases=['stability'])
    async def release(self, ctx, console=None):
        """Posts the stable release binaries for <console>."""
        pass

    @commands.guild_only()
    @commands.command(name='nightly')
    async def nightly(self, ctx, console=None):
        """Posts the nightly release binaries for <console>."""
        pass

    @commands.guild_only()
    @commands.command(name='issue_search')
    async def issue_search(self, ctx, criteria):
        """Search the repository Issues for <criteria>."""
        pass


def setup(bot):
    bot.add_cog(GitHub(bot))
