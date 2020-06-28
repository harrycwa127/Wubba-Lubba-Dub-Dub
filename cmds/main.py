import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import datetime
import random


class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"ping {round(self.bot.latency*1000)} ms")
        print(f"{datetime.datetime.utcnow()} ping {round(self.bot.latency*1000)} ms")


    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title="Introduction",
            description="This is a bot for testing and learning",
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
        print(f"{datetime.datetime.now()} send info of bot")

    @commands.command()
    async def said_by(self, ctx, member, *, msg):
        await ctx.message.delete()
        await ctx.send(f"**{member}** said {msg}")
        print(f"{datetime.datetime.now()} send: **{member}** said {msg}")

    @commands.command()
    async def said(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)
        print(f"{datetime.datetime.now()} send:", msg)

    @commands.command()
    async def del_msg(self, ctx, num: int):
        await ctx.channel.purge(limit=num + 1)
        print(f"{datetime.datetime.now()} del {num} msg ")

    @commands.command()
    async def ran_squad(self, ctx):
        online = []
        ran_online = []

        for member in ctx.guild.members:
            if str(member.status) == "online":
                online.append(member.name)

        ran_online = random.sample(online, k=6)
        for i in range(2):
            temp = random.sample(ran_online, k=3)
            await ctx.send(f"team{i+1}: {str(temp)}")
            for j in temp:
                ran_online.remove(j)


def setup(bot):
    bot.add_cog(Main(bot))