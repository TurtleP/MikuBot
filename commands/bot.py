import discord
from discord.ext import commands
from sys import argv

class Staff:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.has_permissions(manage_messages=True)
    @commands.command(hidden=True)
    async def reload(self):
        

def setup(bot):
    bot.add_cog(Staff(bot))