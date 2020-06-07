import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["channel"]))
        await channel.send(f"{member} join!")
        print(f"{member} join!")


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["channel"]))
        await channel.send(f"{member} leave!")
        print(f"{member} leave!")


    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("hi") and msg.author != self.bot.user:
            await  msg.channel.send(f"**{msg.author.display_name}** hi")
            print(f"**{msg.author.display_name}** hi")

        if msg.content.endswith("bye") and msg.author != self.bot.user:
            await  msg.channel.send(f"**{msg.author.display_name}** bye")
            print(f"**{msg.author.display_name}** bye")

def setup(bot):
    bot.add_cog(Event(bot))
