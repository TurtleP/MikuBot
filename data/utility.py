extensions = ["admin", "wiki"]


def is_staff(ctx):
    if not ctx.guild:
        return False

    user_roles = ctx.author.roles
    return any(r.name == "staff" for r in user_roles)
