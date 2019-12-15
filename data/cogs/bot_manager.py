import re
import subprocess
import traceback

import discord
from discord.ext import commands
from discord.ext.commands import Cog

from data.utility import extensions, is_bot_manager, set_ext_status


class BotManager(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_reload = None

    @commands.guild_only()
    @commands.check(is_bot_manager)
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
                    url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
                embed.description = f"```git\n{output.stdout}```"

                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(str(e))

        await ctx.send("Reloading cogs..")

        for extension in extensions:
            reload_command = self.bot.get_command("reload")

            if reload_command:
                await reload_command.callback(self, ctx, extension, True)

    @commands.guild_only()
    @commands.check(is_bot_manager)
    @commands.command(name='reload')
    async def reload(self, ctx, ext=None, is_update=False):
        """Reloads a specific cog."""
        if not ext:
            ext = self.last_reload

            if not self.last_reload:
                return

        exists = any(extension == ext for extension in extensions)

        if not exists:
            await ctx.send(f":x: Cannot reload `{ext}`. Cog does not exist.")
            return

        try:
            self.bot.unload_extension(f"data.cogs.{ext}")
            self.bot.load_extension(f"data.cogs.{ext}")

            await ctx.send(f":white_check_mark: `{ext}` was reloaded.")

            if not is_update:
                self.last_reload = ext
        except:
            await ctx.send(f":x: `{ext}` failed to load.\n```Traceback:\n{traceback.format_exc()}```\n")
            return

    @commands.guild_only()
    @commands.check(is_bot_manager)
    @commands.command(name='load')
    async def load(self, ctx, ext):
        """Loads a specific cog."""
        exists = any(extension == ext for extension in extensions)

        if not exists:
            await ctx.send(f":x: Cannot reload `{ext}`. Cog does not exist.")
            return

        try:
            self.bot.load_extension(f"data.cogs.{ext}")
            set_ext_status(ext, True)
        except:
            set_ext_status(ext, True)


def setup(bot):
    bot.add_cog(BotManager(bot))
