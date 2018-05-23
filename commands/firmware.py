# firmware.py
# switch firmware commands

import discord
from discord.ext import commands
from sys import argv
import re

class Firmware:
    def __init__(self, bot):
        self.bot = bot

    #firmware
    @commands.command(pass_context=True)
    async def firmware(self, ctx):
        """
            Sets a user's firmware version
            This applies to the range of the firmware:
            e.g. 4.0.0 is 4.0.0 - 4.1.0
        """

        cmd_split = ctx.message.content.split(" ")
        user = ctx.message.author

        if cmd_split and len(cmd_split) > 1:
            if cmd_split[1] == "list":
                await self.bot.say(self.list_users())
            else:
                role = discord.utils.get(self.bot.server.roles, name=cmd_split[1])

                if role is None:
                    await self.bot.say("Could not find firmware '" + cmd_split[1] + "' in the list!")
                else:
                    if not self.has_role(user, role):
                        await self.bot.add_roles(user, role)
                        await self.bot.say("<:lovepotion:417143423523487754> " + user.display_name + " is on Firmware v" + cmd_split[1] + "!")
    
    def list_users(self):
        user_list = {}
        for user in self.bot.server.members:
            for index in range(len(self.bot.firmwares)):
                if self.has_role(user, self.bot.firmwares[index]):
                    if not self.bot.firmwares[index] in user_list:
                        user_list[self.bot.firmwares[index]] = list()

                    user_list[self.bot.firmwares[index]].append(user.display_name)

        output = "```"
        for firmware in user_list:
            output += firmware + ":\n"
            for index in range(len(user_list[firmware])):
                output += "  " + user_list[firmware][index] + "\n"
            output += "\n"
        output += "```"
        return output

    def has_role(self, user, check_role):
        has_role = False
        for role in user.roles:
            if str(role) == str(check_role):
                has_role = True
                break
                
        return has_role

def setup(bot):
    bot.add_cog(Firmware(bot))