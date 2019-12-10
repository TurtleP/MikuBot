import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Wiki(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name='wiki')
    async def wiki(self, ctx):
        """Display the Wiki URL"""
        await ctx.send("https://turtlep.github.io/LovePotion/wiki/#/")

def setup(bot):
    bot.add_cog(Wiki(bot))
