import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import youtube_dl

class Music(Cog_Extension):
    @commands.command()
    async def play(self, ctx, url:str):
        if not ctx.author.voice:
            print(f"{datetime.datetime.now()} client is not in a voice channel!")
            await ctx.send("you must be in a voice channel to play music")

        else:
            player = discord.FFmpegPCMAudio(url)
            if not ctx.voice_client.is_playing():
                await ctx.voice_client.play(player, after = None)
    
    @commands.command()
    async def join(self, ctx):
        print(f"{datetime.datetime.now()} join voice channel {ctx.author.voice.channel.name}")
        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        print(f"{datetime.datetime.now()} leave voice channel {ctx.author.voice.channel.name}")
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Music(bot))