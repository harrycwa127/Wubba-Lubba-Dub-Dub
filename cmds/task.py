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

        self.counter = True

        @commands.Cog.listener()
        async def on_ready():
            self.channel = self.bot.get_channel(int(jdata["channel"]))
            await self.channel.send(">> Wubba Lubba Dub-Dub is online <<")

        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(int(jdata["channel"]))
        #     while not self.bot.is_closed():
        #         await self.channel.send(">> Wubba Lubba Dub-Dub is online <<")
        #         print(
        #             f"{datetime.datetime.utcnow()} loop: >> Wubba Lubba Dub-Dub is online <<"
        #         )
        #         await asyncio.sleep(3600)  # sec

        # async def time_task():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(int(jdata["channel"]))
        #     while not self.bot.is_closed():
        #         now_time = datetime.datetime.utcnow().strftime("%H%M")
        #         if now_time == jdata["time"] and self.counter == True:
        #             await self.channel.send(jdata["statement"])
        #             print(f"{datetime.datetime.utcnow()} time_task: Reminder")
        #             self.counter = False
        #         else:
        #             self.count = 0
        #         await asyncio.sleep(1)

        # self.bg_task = self.bot.loop.create_task(interval())
        # self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        jdata["channel"] = ch
        await ctx.send(f"Set Channel: {self.channel.mention}")
        print(f"{datetime.datetime.utcnow()} Set Channel: {self.channel}")
        with open("Setting.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=len(jdata))

    @commands.command()
    async def alarm(self, ctx, time, *, state: str):
        self.counter = True
        jdata["time"] = time
        jdata["statement"] = state
        with open("setting.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=len(jdata))
        await ctx.send(f"Set alarm: {time} {state}")
        print(f"{datetime.datetime.utcnow()} Set alarm: {time} {state}")


def setup(bot):
    bot.add_cog(Task(bot))
