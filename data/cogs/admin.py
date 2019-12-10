import discord
from discord.ext import commands
from discord.ext.commands import Cog

from data.utility import is_staff

class Staff(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.check(is_staff)
    @commands.command(name='exit', aliases=['quit'])
    async def _exit(self, ctx):
        """Shut down the bot. Staff only."""
        await ctx.send(":wave: Goodbye!")
        await self.bot.logout()

    @commands.guild_only()
    @commands.check(is_staff)
    @commands.command(name='clear', aliases=['erase'])
    async def erase(self, ctx):
        """Clean up messages. Staff only."""
        message_split = ctx.message.content.split(" ")

        limit = 1
        if len(message_split) > 1:
            limit = int(message_split[1])

        async for message in ctx.channel.history(limit=limit + 1):
            await message.delete(delay=1)

def setup(bot):
    bot.add_cog(Staff(bot))
