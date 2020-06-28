import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import youtube_dl
import os
from discord.utils import get


class Music(Cog_Extension):
    @commands.command()
    async def play(self, ctx, url: str):
        song_there = os.path.isfile("song.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            try:
                if song_there:
                    os.remove("song.mp3")
            except PermissionError:
                await ctx.send(
                    "Wait for the current playing music end!"
                )

            ydl_opts = {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
            voice.volume = 75
            voice.is_playing()

        else:
            await ctx.send("pls let me join a voice channel first!")
            print(f"{datetime.datetime.now()}play music fail, not in a voice channel")

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
