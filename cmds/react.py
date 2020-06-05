import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.command()
    async def icon(self, ctx):
        pic = discord.File(jdata["icon"])
        await ctx.send(file=pic)

    @commands.command()
    async def lick(self, ctx, member):
        random_web = random.choice(jdata["lick"])
        await ctx.send(f"{member} you licked by **{ctx.message.author.display_name}**")
        await ctx.send(random_web)

    @commands.command()
    async def roll(self, ctx):
        await ctx.send(f"**{ctx.message.author.display_name}** roll a number from 0 to 100:{random.randint(0, 100)}")


def setup(bot):
    bot.add_cog(React(bot))
