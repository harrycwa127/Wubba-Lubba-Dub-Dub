import discord
from discord.ext import commands
from discord.utils import get
from core.classes import Cog_Extension
import datetime
import youtube_dl
import os


class Music(Cog_Extension):
    @commands.command()
    async def play(self, ctx, url: str):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
            
        if voice and voice.is_connected():
            try:
                if os.path.isfile("song.mp3"):
                    os.remove("song.mp3")
            except PermissionError:
                await ctx.send("Wait for the current playing music end!")

            ytdl_opts = {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }

            if not (voice and voice.is_playing()):
                with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
                    ydl.download([url])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")

            voice.volume = 5
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
        else:
            await ctx.send("Pls let me join a channel!")
            print(
                f"{datetime.datetime.now()} play music fail, still not join a voice channel"
            )


    @commands.command()
    async def stop(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected() and voice.is_playing():
            voice.stop()
            await ctx.send("Stop playing music!")
            print(f"{datetime.datetime.now()} stop playing music")
        else:
            await ctx.send("Stop playing music fail!")
            print(f"{datetime.datetime.now()} stop playing music fail")

    @commands.command()
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected() and voice.is_playing():
            voice.pause()
            await ctx.send("Pause music!")
            print(f"{datetime.datetime.now()} pause music")
        else:
            await ctx.send("Pause music fail!")
            print(f"{datetime.datetime.now()} pause music fail")

    @commands.command()
    async def resume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected() and voice.is_paused():
            voice.resume()
            await ctx.send("Resume paused music!")
            print(f"{datetime.datetime.now()} resume paused music")
        else:
            await ctx.send("Resume paused music fail!")
            print(f"{datetime.datetime.now()} resume paused music fail")

    @commands.command()
    async def playh(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if "song.mp3" in os.listdir("./") and voice and voice.is_connected():
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
            print(f"{datetime.datetime.now()} play past music")

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
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            print(
                f"{datetime.datetime.now()} leave voice channel {ctx.author.voice.channel.name}"
            )
            await ctx.voice_client.disconnect()
        else:
            print(f"{datetime.datetime.now()}leave channel fail!")
            await ctx.send("I am not a channel, can't leave!")


def setup(bot):
    bot.add_cog(Music(bot))
