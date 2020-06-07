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
                print("loop: >> Wubba Lubba Dub-Dub is online <<")
                await asyncio.sleep(3600) #sec
        
        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f"Set Channel: {self.channel.mention}")
        print(f"Set Channel: {self.channel}")

def setup(bot):
    bot.add_cog(Task(bot))