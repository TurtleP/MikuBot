# staff.py
# Staff-only commands

import discord
from discord.ext import commands
from sys import argv
    
class Staff:
    def __init__(self, bot):
        self.bot = bot
    
    #sudo
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def sudo(self, ctx):
        """Sets a staff member to Sudo"""
        user = ctx.message.author

        has_role = False
        for role in user.roles:
            if role == self.bot.sudo_role:
                has_role = True
                break
        
        if self.has_role(user, self.bot.sudo_role):
            await self.bot.remove_roles(user, self.bot.sudo_role)
            await self.bot.say(self.bot.username.lower() + "bot" + user.mention + " ~$ sudo has been revoked!")
        else:
            await self.bot.add_roles(user, self.bot.sudo_role)
            await self.bot.say(self.bot.username.lower() + "bot" + user.mention + " ~$ sudo has been activated!")

    #staff
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def staff(self, ctx):
        """Add/Remove a staff member"""
        try:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                await self.bot.say("Please mention a user.")
                return
                
            if self.has_role(user, self.bot.staff_role):
                await self.bot.remove_roles(user, self.bot.staff_role)
                await self.bot.say("Requim in spaghetti, " + user.mention + "!")
            else:
                await self.bot.add_roles(user, self.bot.staff_role)
                await self.bot.say("Welcome to the Shadow Realm, " + user.mention + "!")
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this!")
    
    #purge
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def purge(self, ctx, arg):
        """Delete messages"""
        channel = ctx.message.channel
        
        to_purge = list(arg)
        
        try:
            amnt = int(to_purge[0])
        except ValueError:
            await self.bot.say("Please specify an amount.")
            return
        
        amnt = min(amnt, 100)
        async for message in self.bot.logs_from(channel, limit=amnt):
            try:
                await self.bot.delete_message(message)
            except discord.errors.Forbidden:
                await self.bot.say(":anger: I don't have permission to do this.")

    #mute
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def mute(self, ctx):
        """(un)Mute a user"""
        try:
            user = ctx.message.mentions[0]
        except IndexError:
            await self.bot.say("Please mention a user.")
            return

        if self.has_role(user, self.bot.mute_role):
            await self.bot.remove_roles(user, self.bot.mute_role)
            await self.bot.say(user.display_name + " has been unmuted!")
        else:
            await self.bot.add_roles(user, self.bot.mute_role)
            await self.bot.say(":anger: " + user.display_name + " has been muted!")

    def has_role(self, user, check_role):
        has_role = False
        for role in user.roles:
            if role == check_role:
                has_role = True
                break
                
        return has_role
        
def setup(bot):
    bot.add_cog(Staff(bot))
