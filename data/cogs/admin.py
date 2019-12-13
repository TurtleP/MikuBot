import re
import subprocess
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
    async def update(self, ctx, method="local"):
        """Reloads all of the bot cogs."""
        if method == "git":
            try:
                await ctx.send("Performing Git pull..")

                embed = discord.Embed(title="Git Update")

                output = subprocess.run(
                    ["git", "pull"], encoding='utf-8', capture_output=True)

                embed.set_thumbnail(
                    url="https://github.blog/wp-content/uploads/2019/01/cropped-github-favicon-512.png?fit=512%2C512")
                embed.description = f"```git\n{output.stdout}```"

                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(str(e))

        await ctx.send("Reloading cogs..")

        for extension in extensions:
            reload_command = self.bot.get_command("reload")

            if reload_command:
                await reload_command.callback(self, ctx, extension)

    @commands.guild_only()
    @commands.check(is_staff)
    @commands.command(name='reload')
    async def reload(self, ctx, ext):
        """Reloads a specific cog."""
        exists = any(extension == ext for extension in extensions)

        if not exists:
            await ctx.send(f":x: Cannot reload `{ext}`. Cog does not exist.")
            return

        try:
            self.bot.unload_extension(f"data.cogs.{ext}")
            self.bot.load_extension(f"data.cogs.{ext}")

            await ctx.send(f":white_check_mark: `{ext}` was reloaded.")
        except:
            await ctx.send(f":x: `{ext}` failed to load.\n```Traceback:\n{traceback.format_exc()}```\n")
            return


def setup(bot):
    bot.add_cog(Staff(bot))
