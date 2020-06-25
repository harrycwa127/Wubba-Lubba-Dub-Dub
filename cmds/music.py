import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import youtube_dl

class Music(Cog_Extension):
    @commands.command()
    async def play(self, ctx, url:str):
        if not ctx.author.voice:
            print(f"{datetime.datetime.utcnow()} client is not in a voice channel!")
            await ctx.send("you must be in a voice channel to play music")

        else:
            pass
    
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice.channel:
            print(f"{datetime.datetime.utcnow()} join voice channel {ctx.author.voice.channel.name}")
            await ctx.author.voice.channel.connect()
        else:
            print("join voice channel fail!")
            await ctx.send("You must in a voice channel!")

    @commands.command()
    async def leave(self, ctx):
        try:
            if ctx.voice_client.is_connected():
                print(f"{datetime.datetime.utcnow()} leave voice channel {ctx.author.voice.channel.name}")
                await ctx.voice_client.disconnect()
        except:
            print(f"{datetime.datetime.utcnow()}leave channel fail!")
            await ctx.send("I am not a channel, can't leave!")


def setup(bot):
    bot.add_cog(Music(bot))