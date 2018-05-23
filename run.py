# MikuBot : Python Edition

bot_description = "A lightweight server administration bot"

# command bot stuff
import discord
from discord.ext import commands

import asyncio
import os
import traceback
import sys
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

prefix = os.environ['prefix']
token = os.environ['token']
username = os.environ['username']

LOAD_HOMEBREW_CMDS = True
firmware_list = [
    "1.0.0", "2.0.0", "3.0.0",
    "4.0.0", "5.0.0"
]

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
    await bot.change_presence(game=discord.Game(name=prefix + "help"))
    
    for server in bot.servers:
        bot.server = server #elite hax
        bot.sudo_role = discord.utils.get(server.roles, name="sudo")
        bot.staff_role = discord.utils.get(server.roles, name="staff")
        bot.mute_role = discord.utils.get(server.roles, name="mute")
        bot.firmwares = firmware_list
        bot.everyone_role = server.default_role

    for firmware in firmware_list:
        if discord.utils.get(server.roles, name=firmware) is None:
            await bot.create_role(bot.server, name=firmware, mentionable=True)

    #loads commands
    commands = [
        "memes",
        "staff",
        "sudo",
        "general"
    ]

    homebrew_commands = [
        "firmware"
    ]

    load_extensions(commands)
    if LOAD_HOMEBREW_CMDS:
        load_extensions(homebrew_commands)

    try:
        await bot.edit_profile(username=('{}'.format(username or "TurtleBot")))
    except discord.errors.Forbidden:
        await bot.say(":anger: I don't have permission to do this!")
    
    print("I'm online! Current date and time: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def load_extensions(command_ext_list):
    for command in command_ext_list:
        try:
            bot.load_extension('commands.' + command)
        except Exception as e:
            print('{} failed to load.\n{}: {}'.format(command, type(e).__name__, e))

bot.run(token)
