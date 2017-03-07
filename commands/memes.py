# meems.py
# Fun commands

import discord
from discord.ext import commands
from sys import argv

class Meme:
    def __init__(self, bot):
        self.bot = bot

    #slap
    @commands.command(pass_context=True)
    async def slap(self, ctx): 
        try:
            author = ctx.message.author
            target = ctx.message.mentions[0]
        except IndexError:
            await self.bot.say("Please mention a user.")
            return

        if target == self.bot.user:
            await self.bot.say("Nice try, " + author.display_name + ".")
        elif author.display_name == target.display_name:
            await self.bot.say("You have slapped yourself. Good job, " + author.display_name + " :ok_hand:")
        else:
            await self.bot.say(target.mention + " has been slapped by " + author.display_name + "!")
    
    #soon:tm:
    @commands.command(pass_context=True)
    async def soon(self, ctx):
        try:
            await self.bot.edit_message(ctx.message, "soon:tm:")
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this.")
    
    #rip
    @commands.command(pass_context=True)
    async def rip(self, ctx):
        try:
            target = ctx.message.mentions[0]
        except IndexError:
            await self.bot.say("React with :regional_indicator_f: to pay respects.")
            return

        if target == self.bot.user:
            await self.bot.say("I'm alive. Don't worry, fam.")
        else:
            await self.bot.say("Pray with :regional_indicator_f: for " + target.display_name)
    
    #lenny
    @commands.command(pass_context=True)
    async def lenny(self, ctx):
        try:
            await self.bot.edit_message(ctx.message, "( ͡° ͜ʖ ͡°)")
        except discord.errors.Forbidden:
            await self.bot.say(":anger: I don't have permission to do this.")

def setup(bot):
    bot.add_cog(Meme(bot))