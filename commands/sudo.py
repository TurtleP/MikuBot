# sudo.py
# sudo commands

import discord
from discord.ext import commands
from sys import argv

class Sudo:
    def __init__(self, bot):
        self.bot = bot

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
            await self.bot.ban(user, 1)
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
    bot.add_cog(Sudo(bot))