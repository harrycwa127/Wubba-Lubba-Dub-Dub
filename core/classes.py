import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __intit__(self, bot):
        self.bot = bot