import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import asyncio
import datetime

with open("setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(int(jdata["channel"]))
            while not self.bot.is_closed():
                await self.channel.send(">> Wubba Lubba Dub-Dub is online <<")
                print(f"{datetime.datetime.now()} loop: >> Wubba Lubba Dub-Dub is online <<")
                await asyncio.sleep(3600) #sec
        
        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        jdata["channel"] = ch
        await ctx.send(f"Set Channel: {self.channel.mention}")
        print(f"{datetime.datetime.now()} Set Channel: {self.channel}")
        with open("Setting.json", "w", encoding = "utf8")as jfile:
            json.dump(jdata, jfile, indent = len(jdata))
    
    @commands.command()
    async def set_time(self, ctx, time):
        jdata["time"] = time
        with open("setting.json", "w", endcoding="utf8") as jfile:
           json.dump(jdata, jfile, indent = len(jdata))
        await ctx.send(f"Set time: {time}")
        print(f"{datetime.datetime.now()} Set time: {time}")

def setup(bot):
    bot.add_cog(Task(bot))