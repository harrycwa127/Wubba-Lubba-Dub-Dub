import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "-")

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(718001395751583764)
    await channel.send(f"{member} join!")
    print(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(718001395751583764)
    await channel.send(f"{member} leave!")
    print(f"{member} leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(bot.latency)

bot.run("NzE3Nzk5OTc3NjQwMDAxNTg2.XtiCEw.41PqWkJ93DiwAcrguwug7FwpR6A")
