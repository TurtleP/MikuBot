import re
import subprocess
import traceback
from datetime import datetime

import discord
from discord.ext import commands
from discord.ext.commands import Cog

from data.utility import (extensions, is_bot_manager,
                          set_ext_status, load_extension,
                          send_embed)


class BotManager(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_reload = None

    def generate_summary(self, title, cog_names):
        embed = discord.Embed(title=f"{title} Summary")
        embed.description = datetime.now().strftime("%c")

        return embed

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
            try:
                self.bot.unload_extension(f"data.cogs.{extension}")
                load_extension(self.bot, extension)
            except:
                pass

        status_command = self.bot.get_command("status")
        await ctx.invoke(status_command)

    async def check_command_exists(self, ctx, command, ext):
        exists = any(extension == ext for extension in extensions)

        if not exists:
            await send_embed(ctx, f"{command} Failure",
                             0xE53935, f"Cannot reload `{ext}`. Cog does not exist.")

    @commands.guild_only()
    @commands.check(is_bot_manager)
    @commands.command(name='reload')
    async def reload(self, ctx, ext=None):
        """Reloads a specific cog."""
        if not ext:
            ext = self.last_reload

            if not self.last_reload:
                return

        if not await self.check_command_exists(ctx, "Reload", ext):
            return

        try:
            self.bot.unload_extension(f"data.cogs.{ext}")
            load_extension(self.bot, ext)

            self.last_reload = ext
        except:
            await send_embed(ctx, "Reload Failure",
                             0xE53935, f"Traceback:\n{traceback.format_exc()}")

    @commands.guild_only()
    @commands.check(is_bot_manager)
    @commands.command(name='load')
    async def load(self, ctx, ext):
        """Loads a specific cog."""
        if not await self.check_command_exists(ctx, "Load", ext):
            return

        is_loaded = load_extension(self.bot, ext)

        if is_loaded:
            await send_embed(ctx, "Load Successful",
                             0x7CB342, f"Loaded Cog `{ext}` successfully.")


def setup(bot):
    bot.add_cog(BotManager(bot))
