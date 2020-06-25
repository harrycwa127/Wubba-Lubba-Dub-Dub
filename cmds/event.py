import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["channel"]))
        await channel.send(f"{member} join!")
        print(f"{datetime.datetime.utcnow()} {member} join!")


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["channel"]))
        await channel.send(f"{member} leave!")
        print(f"{datetime.datetime.utcnow()} {member} leave!")


    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("hi") and msg.author != self.bot.user:
            await  msg.channel.send(f"{msg.author.mention} hi")
            print(f"{datetime.datetime.utcnow()} {msg.author.mention} hi")

        if msg.content.endswith("bye") and msg.author != self.bot.user:
            await  msg.channel.send(f"{msg.author.mention} bye")
            print(f"{datetime.datetime.utcnow()} {msg.author.mention} bye")

def setup(bot):
    bot.add_cog(Event(bot))
