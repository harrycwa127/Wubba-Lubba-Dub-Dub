import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import youtube_dl
import os


class Music(Cog_Extension):
    @commands.command()
    async def play(self, ctx, url:str):
        if not ctx.author.voice:
            print(f"{datetime.datetime.now()} client is not in a voice channel!")
            await ctx.send("you must be in a voice channel to play music")

        else:
            song_there = os.path.isfile("song.mp3")

            try:
                if song_there:
                    os.remove("song.mp3")

            except PermissionError:
                await ctx.send("Wait for the current playing music end or use the 'stop' command")
                
            await ctx.send("Getting everything ready, playing audio soon")
            print("Someone wants to play music let me get that ready for them...")
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url)
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, 'song.mp3')
            ctx.voice_client.play(discord.FFmpegPCMAudio("song.mp3"))
            ctx.voice_client.volume = 100
            ctx.voice_client.is_playing()

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice.channel:
            print(
                f"{datetime.datetime.now()} join voice channel {ctx.author.voice.channel.name}"
            )
            await ctx.author.voice.channel.connect()
        else:
            print("join voice channel fail!")
            await ctx.send("You must in a voice channel!")

    @commands.command()
    async def leave(self, ctx):
        try:
            if ctx.voice_client.is_connected():
                print(
                    f"{datetime.datetime.now()} leave voice channel {ctx.author.voice.channel.name}"
                )
                await ctx.voice_client.disconnect()
        except:
            print(f"{datetime.datetime.now()}leave channel fail!")
            await ctx.send("I am not a channel, can't leave!")


def setup(bot):
    bot.add_cog(Music(bot))