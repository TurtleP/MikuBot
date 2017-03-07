# MikuBot : Python Edition

bot_description = "A lightweight server administration bot"

# command bot stuff
import discord
from discord.ext import commands

import asyncio
import os
import traceback
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

prefix = os.environ['prefix']
token = os.environ['token']
username = os.environ['username']

bot = commands.Bot(prefix, description=bot_description, pm_help=None)

# set avatar on load
avatar_file = open('media/avatar.png', 'rb')

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass  # ...don't need to know if commands don't exist
    elif isinstance(error, discord.ext.commands.errors.CheckFailure):
        await bot.send_message(ctx.message.channel, "{} You don't have permission to use this command.".format(ctx.message.author.mention))
    else:
        if ctx.command:
            await bot.send_message(ctx.message.channel, "An error occured while processing the `{}` command.".format(ctx.command.name))
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@bot.event
async def on_ready():

    await bot.edit_profile(password=(None), avatar=(avatar_file.read()))

    await bot.change_presence(game=discord.Game(name=prefix + "help"))

    bot.username = username
    
    for server in bot.servers:
        bot.server = server #elite hax
        bot.sudo_role = discord.utils.get(server.roles, name="sudo")
        bot.staff_role = discord.utils.get(server.roles, name="staff")
        bot.everyone_role = server.default_role

    try:
        await bot.edit_profile(username=('{}'.format(username or "TurtleBot")))
    except discord.errors.Forbidden:
        await bot.say(":anger: I don't have permission to do this!")

# loads commands
commands = [
    "memes",
    "staff"
]

for command in commands:
    try:
        bot.load_extension('commands.' + command)
    except Exception as e:
        print('{} failed to load.\n{}: {}'.format(command, type(e).__name__, e))

bot.run(token)