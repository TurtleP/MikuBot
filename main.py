#!/usr/bin/python3

import os

import discord
from discord.ext import commands

from data.utility import extensions

bot_description = "A lightweight server bot for Tiny Turtle Industries"

# Get our environment variables
BOT_PREFIX = os.environ['BOT_PREFIX']
BOT_TOKEN = os.environ['BOT_TOKEN']

# Create a new Bot instance
bot = commands.Bot(BOT_PREFIX, description=bot_description)

for item in extensions:
    bot.load_extension(f"data.cogs.{item}")


@bot.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.CommandNotFound):
        return await ctx.send(error)

    if isinstance(error, commands.MissingPermissions):
        return await ctx.send("You don't have the right permissions to use this command!")

bot.run(BOT_TOKEN)
