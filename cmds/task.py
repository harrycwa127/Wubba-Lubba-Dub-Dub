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
            await self.bot.wait_unit_ready()
            self.channel = self.bot.get_channel(int(jdata["channel"]))
            while not self.bot.is_closed():
                await self.channel.send("I am still alive!")
                print("loop: I am still alive")
                await asyncio.sleep(10) #sec
        
        self.bg_task = self.bot.loop.create_task(interval())


def setup(bot):
    bot.add_cog(Task(bot))