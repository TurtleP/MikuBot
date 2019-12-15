import json

import discord
from discord.ext import commands

extensions = {
    "bot_manager": None,
    "general":     None,
    "github":      None,
    "staff":       None,
    "wiki":        None
}

with open("data/embeds.json") as file:
    embed_json = json.load(file)

with open("config.json") as file:
    config_json = json.load(file)


def load_extension(bot, which):
    try:
        bot.load_extension(f"data.cogs.{which}")
        set_ext_status(which, True)
    except commands.ExtensionFailed:
        set_ext_status(which, False)
        return
    except commands.ExtensionAlreadyLoaded:
        return

    return True

async def send_embed(ctx, title, color=None, description=None):
    embed = discord.Embed(title=title)

    embed.description = description
    embed.colour = color

    await ctx.send(embed=embed)


def set_ext_status(which, success=False, embed=False):
    success = "✓"
    failure = "×"

    if which in extensions:
        if success:
            dict.update(extensions, {f"{which}":
                                     f"{success} Online"})
        else:
            dict.update(extensions, {f"{which}":
                                     f"{failure} Error"})


def get_embed_data(which):
    if which in embed_json:
        return embed_json[which]

    return None


def get_config_data(which):
    if which in config_json:
        return config_json[which]


def get_role_id(which):
    role_ids = get_config_data("roles")

    if which in role_ids:
        return role_ids[which]


def is_staff(ctx):
    if not ctx.guild:
        return False

    user_roles = ctx.author.roles
    return any(r.id == get_role_id("staff") for r in user_roles)


def is_bot_manager(ctx):
    if not ctx.guild:
        return False

    user_roles = ctx.author.roles
    return any(r.id == get_role_id("bot manager") for r in user_roles)


def is_developer(ctx):
    if not ctx.guild:
        return False

    user_roles = ctx.author.roles
    return any(r.id == get_role_id("developer") for r in user_roles)
