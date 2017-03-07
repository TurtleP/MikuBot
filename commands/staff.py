# staff.py
# Staff-only commands

import discord
from discord.ext import commands
from sys import argv

class Staff:
    def __init__(self, bot):
        self.bot = bot

    #addstaff
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def addstaff(self, ctx):
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
                
            if has_role:
                await self.bot.say(user.display_name + " is already staff!")
            else:
                await self.bot.add_roles(user, self.bot.staff_role)
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this!")

    #delstaff
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def delstaff(self, ctx):
        try:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                await self.bot.say("Please mention a user.")
                return
                
            staff_role = self.bot.server.roles.find("staff")

            if not user.roles.find(staff_role):
                await self.bot.say(user.display_name + " is not staff!")
                return

            await self.bot.remove_roles(user, staff_role)
            await self.bot.say("Requim in spaghetti, " + user.display_name + "!")
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this!")

    #ban
    @commands.has_permissions(administrator=True)
    @commands.command(pass_context=True)
    async def ban(self, ctx):
        try:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                await self.bot.say("Please mention a user.")
                return

            reason = ctx.mentions.split("' '", 1)

            if user is None:
                return

            if not reason is None:
                await self.bot.send_message(user, "You have been banned from " + ctx.server.name + "! Reason: " + reason)
            else:
                await self.bot.send_message(user, "You have been banned from " + ctx.server.name + "!")

            await self.bot.ban(user, 1)
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this!")

    #lockdown (toggle)
    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def lockdown(self, ctx):
        try:
            permission = ctx.message.channel.overwrites_for('@everyone')
            if permission.send_messages == False:
                permission.send_messages = True

                await self.bot.edit_channel_permissions(ctx.message.channel, '@everyone', permission)
                await self.bot.say("Thanks for your co-operation! :wave:")
                return

            permission.send_messages = False
            await self.bot.edit_channel_permissions(ctx.message.channel, '@everyone', permission)
            await self.bot.say("Channel has been locked down! Only Staff may speak.")
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this.")

def setup(bot):
    bot.add_cog(Staff(bot))