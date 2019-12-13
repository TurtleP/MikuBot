import json

extensions = ["staff", "wiki", "bot_manager"]

with open("data/embeds.json") as file:
    embed_json = json.load(file)

def get_embed_data(which):
    if which in embed_json:
        return embed_json[which]

    return None

def is_staff(ctx):
    if not ctx.guild:
        return False

    user_roles = ctx.author.roles
    return any(r.name == "staff" for r in user_roles)

def is_bot_manager(ctx):
    if not ctx.guild:
        return False

    user_roles = ctx.author.roles
    return any(r.name == "bot manager" for r in user_roles)
