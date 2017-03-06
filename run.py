# MikuBot : Python Edition

botDescription = "Miku: A lightweight server administration bot"

# command bot stuff
from discord.ext import commands

import discord
import asyncio
import os

bot = commands.Bot(command_prefix=os.environ['prefix'], description=botDescription, pm_help=None)

# set avatar on load
@bot.event
async def on_ready():
    avatar = open('media/avatar.jpg', 'rb')
    bot.edit_profile(password=None, avatar=avatar.read())


# loads commands
commands = []
failed = []

for command in commands:
    try:
        bot.load_extension('commands.' + command)
    except Exception as e:
        print('{} failed to load.\n{}: {}'.format(command, type(e).__name__, e))
        failed_addons.append([command, type(e).__name__, e])

bot.run(os.environ['token'])