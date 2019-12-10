#!/usr/bin/python3

from discord.ext import commands
import discord
import os

bot_description = "A lightweight server administration bot"

# Get our environment variables
BOT_PREFIX = os.environ['BOT_PREFIX']
BOT_TOKEN = os.environ['BOT_TOKEN']

# Create a new Bot instance
bot = commands.Bot(BOT_PREFIX, description=bot_description, pm_help=None)

bot.load_extension("data.cogs.admin")

@bot.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.CommandNotFound):
        return await ctx.send(error)

    if isinstance(error, commands.MissingPermissions):
        return await ctx.send("You don't have the right permissions to use this command!")

bot.run(BOT_TOKEN)
