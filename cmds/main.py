import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} ms")

    @commands.command()
    async def sum(self, ctx, num1:int, num2:int):
        await ctx.send(f"The sum of 2 numbers is {num1+num2}")

    @commands.command()
    async def dir(self, ctx):
        for filename in os.listdir("./cmds"):
            await ctx.send(filename)


def setup(bot):
    bot.add_cog(Main(bot))
