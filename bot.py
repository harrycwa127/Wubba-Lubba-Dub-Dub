import discord
from discord.ext import commands
import json
import random

with open("setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="-")


@bot.event
async def on_ready():
    channel = bot.get_channel(int(jdata["channel"]))
    await channel.send(">> Wubba Lubba Dub-Dub is online <<")
    print(">> Wubba Lubba Dub-Dub is online <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["channel"]))
    await channel.send(f"{member} join!")
    print(f"{member} join!")


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["channel"]))
    await channel.send(f"{member} leave!")
    print(f"{member} leave!")


@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}ms")


@bot.command()
async def icon(ctx):
    pic = discord.File(jdata["icon"])
    await ctx.send(file=pic)


@bot.command()
async def lick(ctx):
    random_web = random.choice(jdata["lick"])
    await ctx.send(random_web)

bot.run(jdata["TOKEN"])
