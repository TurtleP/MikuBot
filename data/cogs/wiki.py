import discord
from discord.ext import commands
from discord.ext.commands import Cog

from data.utility import get_embed_data


class Wiki(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name='wiki')
    async def wiki(self, ctx):
        """Display the Wiki URL"""
        await ctx.send("https://turtlep.github.io/LovePotion/wiki/#/")

    @commands.guild_only()
    @commands.command(name="faq")
    async def faq(self, ctx):
        """Display the Wiki FAQ URL"""
        await ctx.send("https://turtlep.github.io/LovePotion/wiki/#/faq")

    @commands.guild_only()
    @commands.command(name="showcase")
    async def showcase(self, ctx):
        """Display the Wiki Showcase URL and Requirements"""

        embed = discord.Embed(title="Löve Potion Showcase",
                              url="https://turtlep.github.io/LovePotion/wiki/#/showcase",
                              description="Submission Instructions")

        showcase_embed_data = get_embed_data("showcase")

        if not showcase_embed_data:
            return

        for index in range(len(showcase_embed_data)):
            embed_item = showcase_embed_data[index]

            embed.add_field(name=f"{index + 1}. {embed_item['title']}",
                            value=embed_item["description"],
                            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Wiki(bot))
