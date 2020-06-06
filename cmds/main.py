import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import datetime


class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"ping {round(self.bot.latency*1000)} ms")

    @commands.command()
    async def sum(self, ctx, num1: int, num2: int):
        await ctx.send(f"The sum of 2 numbers is {num1+num2}")

    @commands.command()
    async def dir(self, ctx):
        for filename in os.listdir("./cmds"):
            await ctx.send(filename)

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title="Introduction",
            description="This is a bot for testing amd learning",
            color=0x04F6E6,
            timestamp=datetime.datetime.utcnow(),
        )
        embed.set_author(
            name="Wubba Lubba Dub-Dub",
            url="https://discord.com/api/oauth2/authorize?client_id=717799977640001586&permissions=0&scope=bot",
            icon_url="https://imgur.dcard.tw/MHVEA6Rh.jpg",
        )
        embed.set_thumbnail(url="https://imgur.dcard.tw/MHVEA6Rh.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def said_by(self, ctx, member, *, msg):
        await ctx.message.delete()
        await ctx.send(f"**{member}** said {msg}")

    @commands.command()
    async def said_byme(self, ctx, member, *, msg):
        await ctx.message.delete()
        await ctx.send(f"**{ctx.message.author.display_name}** said {msg}")

    @commands.command()
    async def said(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def del_msg(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)


def setup(bot):
    bot.add_cog(Main(bot))
