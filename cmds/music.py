import discord
from discord.ext import commands
from discord.utils import get
from core.classes import Cog_Extension
import datetime
import youtube_dl
import os 
import shutil


class Music(Cog_Extension):
    queues = {} 

    @commands.command(aliases = ["p"], description = "play music")
    async def play(self, ctx, url: str):

        def check_q():
            if os.path.isdir("./Music Queue"):
                DIR = os.path.abspath(os.path.realpath("Music Queue"))

                try:
                    first_file = os.listdir(DIR)[0]
                except:
                    print(f"{datetime.datetime.now()} No more song in the queue")
                    self.queues.clear()
                    return

                if len(os.listdir("./Music Queue")) > 0:
                    if os.path.isfile("song.mp3"):
                        os.remove("song.mp3") 

                    shutil.move(os.path.abspath(os.path.realpath("Music Queue") + f"/{first_file}") ,os.path.abspath(os.path.realpath("./")))
                    
                    for file in os.listdir("./"):
                         if file.endswith(".mp3"):
                            os.rename(file, "song.mp3")

                    voice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_q())
                    voice.source = discord.PCMVolumeTransformer(voice.source, volume = 0.08 )

                else:
                    self.queues.clear()
                    return
            else:
                self.queues.clear()


        voice = get(self.bot.voice_clients, guild=ctx.guild)
            
        if voice and voice.is_connected():
            try:
                if os.path.isfile("song.mp3"):
                    os.remove("song.mp3")
            except PermissionError:
                await ctx.send("Wait for the current playing music end!")
                return

            try:
                if os.path.isdir("./Music Queue"):
                    shutil.rmtree("./Music Queue")
            except:
                print("No old Queue folder")

            ytdl_opts = {
                "format": "bestaudio/best",
                "quiet": True,
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


            voice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_q())
            voice.source = discord.PCMVolumeTransformer(voice.source, volume = 0.08)
        else:
            await ctx.send("Pls let me join a channel!")
            print(
                f"{datetime.datetime.now()} play music fail, still not join a voice channel"
            )
    

    @commands.command(aliases = ['q'], description = "show the music queue")
    async def queue(self, ctx, url: str):
        if os.path.isdir("./Music Queue") is False:
            os.mkdir("Music Queue")

        DIR = os.path.abspath(os.path.realpath("Music Queue"))
        q_num = len(os.listdir(DIR)) + 1
        add_q = True
        while add_q:
            if q_num in self.queues:
                q_num += 1
            else:
                add_q = False
                self.queues[q_num] = q_num
        
        q_path = os.path.abspath(os.path.realpath("Music Queue") + f"/song{q_num}.%(ext)s")

        ytdl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "outtmpl": q_path,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
            ydl.download([url])

        print(f"{datetime.datetime.now()} add song to the queue")
        await ctx.send(f"add song {q_num} to the queue")




    @commands.command(description = "stop playing music")
    async def stop(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        self.queues.clear()

        if voice and voice.is_connected() and voice.is_playing():
            voice.stop()
            await ctx.send("Stop playing music!")
            print(f"{datetime.datetime.now()} stop playing music")
        else:
            await ctx.send("Stop playing music fail!")
            print(f"{datetime.datetime.now()} stop playing music fail")

    @commands.command(description = "pause music")
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected() and voice.is_playing():
            voice.pause()
            await ctx.send("Pause music!")
            print(f"{datetime.datetime.now()} pause music")
        else:
            await ctx.send("Pause music fail!")
            print(f"{datetime.datetime.now()} pause music fail")

    @commands.command(description = "resume music")
    async def resume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected() and voice.is_paused():
            voice.resume()
            await ctx.send("Resume paused music!")
            print(f"{datetime.datetime.now()} resume paused music")
        else:
            await ctx.send("Resume paused music fail!")
            print(f"{datetime.datetime.now()} resume paused music fail")

    @commands.command(aliases = ["pd"], description = "stop play downloaded music")
    async def playd(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if "song.mp3" in os.listdir("./") and voice and voice.is_connected():
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
            print(f"{datetime.datetime.now()} play past music")

    @commands.command(aliases = ["j"], description = "join voice channel")
    async def join(self, ctx):
        if ctx.author.voice.channel:
            print(
                f"{datetime.datetime.now()} join voice channel {ctx.author.voice.channel.name}"
            )
            await ctx.author.voice.channel.connect()
        else:
            print("join voice channel fail!")
            await ctx.send("You must in a voice channel!")

    @commands.command(aliases = ["l"], description = "leave voice channel")
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
