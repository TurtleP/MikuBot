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
        
        if has_role:
            await self.bot.remove_roles(user, self.bot.sudo_role)
            await self.bot.say(self.bot.username.lower() + "bot" + user.mention + " ~$ sudo has been revoked!")
        else:
            await self.bot.add_roles(user, self.bot.sudo_role)
            await self.bot.say(self.bot.username.lower() + "bot" + user.mention + " ~$ sudo has been activated!")

    #addstaff
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def addstaff(self, ctx):
        """Add a staff member"""
        try:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                await self.bot.say("Please mention a user.")
                return

            has_role = False
            for role in user.roles:
                print(role, self.bot.staff_role)
                if role == self.bot.staff_role:
                    has_role = True
                    break
                
            if has_role:
                await self.bot.say(user.display_name + " is already staff!")
            else:
                await self.bot.add_roles(user, self.bot.staff_role)
                await self.bot.say("Welcome to the Shadow Realm, " + user.mention + "!")
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this!")

    #delstaff
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def delstaff(self, ctx):
        """Remove a staff member"""
        try:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                await self.bot.say("Please mention a user.")
                return

            has_role = False
            for role in user.roles:
                if role == self.bot.staff_role:
                    has_role = True
                    break
                
            if not has_role:
                await self.bot.say(user.display_name + " is not staff!")
            else:
                await self.bot.remove_roles(user, self.bot.staff_role)
                await self.bot.say("Requim in spaghetti, " + user.mention + "!")
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this!")
    
    #bans
    @commands.command()
    async def bans(self):
        """List banned users"""
        banned_users = await self.bot.get_bans(self.bot.server)
        if banned_users is None:
            await self.bot.say("No banned users have been found.")
        else:
            names = ""
            for i in range(len(banned_users)):
                names = names + banned_users[i].name + " "
            await self.bot.say(names)

    #ban
    @commands.has_permissions(administrator=True)
    @commands.command(pass_context=True)
    async def ban(self, ctx, *msg):
        """Ban a user"""
        try:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                await self.bot.say("Please mention a user.")
                return
            
            reason = list(msg)

            reason.pop(0)

            add_string = ""
            if len(reason) > 0:
                add_string = " Reason: " + ' '.join(reason)
            
            await self.bot.send_message(user, "You have been banned from " + self.bot.server.name + "!" + add_string)

            #await self.bot.ban(user, 1)
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this!")

    #unban
    @commands.has_permissions(administrator=True)
    @commands.command(pass_context=True)
    async def unban(self, ctx):
        """Unban a user"""
        try:
            user = ctx.message.content.split(" ")[1]
            
            bans = await self.bot.get_bans(self.bot.server)
            
            for i in range(len(bans)):
                if bans[i].name == user:
                    await self.bot.unban(self.bot.server, bans[i])
                    await self.bot.say(bans[i].name + " has been unbanned!")
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this!")

    #kick
    @commands.has_permissions(administrator=True)
    @commands.command(pass_context=True)
    async def kick(self, ctx, *msg):
        """Kick a user"""
        try:
            user = ctx.message.mentions[0]
        except IndexError:
            self.bot.say("Please mention a user.")
            return

        reason = list(msg)

        reason.pop(0)

        add_string = ""
        if len(reason) > 0:
            add_string = " Reason: " + ' '.join(reason)

        await self.bot.send_message(user, "You have been kicked from " + self.bot.server.name + "!" + add_string)

        self.bot.kick(user)
    
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
        
        try:
            amnt = min(amnt, 100)
            await self.bot.purge_from(channel, limit=amnt, check=None)
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this.")

    #lockdown (toggle)
    @commands.has_permissions(administrator=True)
    @commands.command(pass_context=True)
    async def lockdown(self, ctx):
        """(un)Lock a channel"""
        try:
            permission = ctx.message.channel.overwrites_for(self.bot.everyone_role)
            if permission.send_messages == False:
                permission.send_messages = True

                await self.bot.edit_channel_permissions(ctx.message.channel, self.bot.everyone_role, permission)
                await self.bot.say("Thanks for your co-operation! :wave:")
                return

            permission.send_messages = False
            await self.bot.edit_channel_permissions(ctx.message.channel, self.bot.everyone_role, permission)
            await self.bot.say("Channel has been locked down! Only Staff may speak.")
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this.")

def setup(bot):
    bot.add_cog(Staff(bot))
