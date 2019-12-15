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
        """Shut down the bot."""
        await ctx.send(":wave: Goodbye!")
        await self.bot.logout()

    @commands.guild_only()
    @commands.check(is_staff)
    @commands.command(name='clear', aliases=['erase'])
    async def erase(self, ctx, limit=1):
        """Clean up messages. Optional count argument."""
        async for message in ctx.channel.history(limit=limit + 1):
            await message.delete(delay=1)

    @commands.check(is_staff)
    @commands.command(name='kick')
    async def kick(self, ctx, _user, reason=None):
        """Kicks a user, optional reason."""

        user = ctx.message.mentions[0]
        if user == self.bot.user:
            await ctx.send("This is why we can't have nice things.")
            return

        try:
            add_string = ""
            if reason:
                add_string = f"Reason: {reason}"

            await user.kick(reason=reason)
            await ctx.send(f"**{user.name}** has been kicked. {add_string}")
        except discord.HTTPException:
            await ctx.send(f"Could not kick user **{user.name}**. They are **_too powerful!_**")

    @commands.check(is_staff)
    @commands.command(name='ban')
    async def ban(self, ctx, _user, reason=None):
        """Kicks a user, optional reason."""

        user = ctx.message.mentions[0]
        if user == self.bot.user:
            await ctx.send("This is why we can't have nice things.")
            return

        try:
            add_string = ""
            if reason:
                add_string = f"Reason: {reason}"

            await user.kick(reason=reason)
            await ctx.send(f"**{user.name}** has been banned. {add_string}")
        except discord.HTTPException:
            await ctx.send(f"Could not ban user **{user.name}**. They are **_too powerful!_**")


def setup(bot):
    bot.add_cog(Staff(bot))
