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

        screenshot_desc = """
        Create a preview screenshot. Nintendo Switch previews should be 1280x720.
        3DS previews should be 400x240 (or 400x480 for both screens).
        """
        embed.add_field(name="1. Screenshot",
                        value=screenshot_desc, inline=False)

        description_desc = """
        Write up a paragraph or two describing your library or game.
        """
        embed.add_field(name="2. Description",
                        value=description_desc, inline=False)

        submit_desc = """
        Go to https://github.com/TurtleP/TurtleP.github.io and submit and Issue.
        Please label it as a Wiki Showcase Submission. Be sure to include
        contributors (if more than two or three, please upload a text file with
        everyone), the title of your library or game, other assets from these
        instructions, and the console it is for.
        """
        embed.add_field(name="3. Submit an Request",
                        value=submit_desc)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Wiki(bot))
