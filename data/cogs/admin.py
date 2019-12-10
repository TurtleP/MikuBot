import re
import traceback

import discord
from discord.ext import commands
from discord.ext.commands import Cog

from data.utility import extensions, is_staff


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
    async def erase(self, ctx, limit=1):
        """Clean up messages. Optional count argument. Staff only."""
        async for message in ctx.channel.history(limit=limit + 1):
            await message.delete(delay=1)

    @commands.guild_only()
    @commands.check(is_staff)
    @commands.command(name='update', aliases=['pull'])
    async def update(self, ctx, from_git=False):
        """Updates the bot. Optional argument allows pulling from git."""
        if from_git:
            await ctx.send("Pulling latest files..")
            git_output = await self.bot.async_call_shell("git pull")
            await ctx.send(f"Complete. Output: ```{git_output}```")

        await ctx.send("Reloading cogs.. Please wait.")

        for extension in extensions:
            try:
                self.bot.unload_extension(f"data.cogs.{extension}")
                self.bot.load_extension(f"data.cogs.{extension}")

                await ctx.send(f":white_check_mark: `{extension}` was reloaded.")
            except:
                await ctx.send(f":x: `{extension}` failed to load. Traceback:\n{traceback.format_exc()}\n")
                return

    @commands.guild_only()
    @commands.check(is_staff)
    @commands.command(name='reload')
    async def reload(self, ctx, ext):
        """Reloads an extension."""
        exists = any(extension == ext for extension in extensions)

        if not exists:
            await ctx.send(f":x: Cannot reload `{ext}`. Cog does not exist.")
            return

        try:
            self.bot.unload_extension(f"data.cogs.{ext}")
            self.bot.load_extension(f"data.cogs.{ext}")
            await ctx.send(f":white_check_mark: `{ext}` was reloaded.")
        except:
            await ctx.send(f":x: `{ext}` failed to load. Traceback:\n{traceback.format_exc()}\n")
            return


def setup(bot):
    bot.add_cog(Staff(bot))
