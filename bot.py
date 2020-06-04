import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "/")

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run("NzE3Nzk5OTc3NjQwMDAxNTg2.XtiCEw.41PqWkJ93DiwAcrguwug7FwpR6A")
