from datetime import datetime

import discord
from discord.ext import commands
from discord.ext.commands import Cog

from data.utility import extensions


class General(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Ping, pong your latency is wrong!"""
        message_time = ctx.message.created_at
        current_time = datetime.now()

        latency = current_time - message_time

        await ctx.send(f":ping_pong:! Pong! Response time: {str(latency.microseconds / 1000.0)} ms")

    @commands.command(name='about')
    async def about(self, ctx):
        """Displays information about the bot."""
        embed = discord.Embed(title="About Potion Böt",
                              url="https://github.com/TurtleP/TurtleBot")
        await ctx.send(embed=embed)

    @commands.command(name='status')
    async def status(self, ctx):
        """Displays the status of cogs."""
        embed = discord.Embed(title="Cog Status")

        current_time = datetime.now().strftime("%c")
        embed.description = current_time

        for item in extensions:
            embed.add_field(name=item,
                            value=extensions[item],
                            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
