# general.py
# general use commands

import discord
from discord.ext import commands
from sys import argv

class General:
    def __init__(self, bot):
        self.bot = bot
    
    #bans
    @commands.command()
    async def bans(self):
        """List banned users"""
        banned_users = await self.bot.get_bans(self.bot.server)
            
        names = ""
        for i in range(len(banned_users)):
            names = names + "``" +  banned_users[i].name + "`` "
    
        if names == "":
            await self.bot.say("No banned users have been found! :ok_hand:")
        else:
            await self.bot.say(names)

def setup(bot):
    bot.add_cog(General(bot))