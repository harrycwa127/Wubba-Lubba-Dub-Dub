import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
import datetime

with open("setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.command()
    async def icon(self, ctx):
        pic = discord.File(jdata["icon"])
        await ctx.send(file=pic)
        print(f"{datetime.datetime.now()} icon")

    @commands.command()
    async def lick(self, ctx, member=None):
        random_web = random.choice(jdata["lick"])
        if member is not None:
            await ctx.send(f"{member} you licked by {ctx.message.author.mention}")
            print(
                f"{datetime.datetime.now()} {member} you licked by {ctx.message.author.mention}"
            )
        else:
            await ctx.send(f"licked by {ctx.message.author.mention}")
            print(f"{datetime.datetime.now()} licked by {ctx.message.author.mention}")
        await ctx.send(random_web)

    @commands.command()
    async def roll(self, ctx):
        ran = random.randint(0, 100)
        await ctx.send(
            f"Roll a number from 0 to 100： {ran}"
        )
        print(f"{datetime.datetime.now()} roll", ran)


def setup(bot):
    bot.add_cog(React(bot))
