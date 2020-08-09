import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
import datetime

with open("setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.command(description = "print out the icon of the bot")
    async def icon(self, ctx):
        pic = discord.File(jdata["icon"])
        await ctx.send(file=pic)
        print(f"{datetime.datetime.now()} icon")

    @commands.command(description = "lick someone or lick yourself")
    async def lick(self, ctx, member=None):
        random_web = random.choice(jdata["lick"])
        if member is not None:
            member = member + " you"
        else:
            member = ""
        
        await ctx.send(f"{member} you licked by {ctx.message.author.mention}")
        print(
            f"{datetime.datetime.now()} {member} you licked by {ctx.message.author.mention}")

    @commands.command(description = "roll a number from 0 to 100")
    async def roll(self, ctx):
        ran = random.randint(0, 100)
        await ctx.send(
            f"Roll a number from 0 to 100： {ran}"
        )
        print(f"{datetime.datetime.now()} roll", ran)


def setup(bot):
    bot.add_cog(React(bot))
