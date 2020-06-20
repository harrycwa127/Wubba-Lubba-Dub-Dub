import discord
from discord.ext import commands
import json
import os
import datetime


with open("setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="/", description="Harry's Bot")


@bot.event
async def on_ready():
    print(f"{datetime.datetime.now()} >> Wubba Lubba Dub-Dub is online <<")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")
    print(f"{datetime.datetime.now()} Loaded {extension} done.")
    
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Un-Loaded {extension} done.")
    print(f"{datetime.datetime.now()} Un-Loaded {extension} done.")
    
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Re-Loaded {extension} done.")
    print(f"{datetime.datetime.now()} Re-Loaded {extension} done.")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")


if __name__ == "__main__":
    bot.run(jdata["TOKEN"])
