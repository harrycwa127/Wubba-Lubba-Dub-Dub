import discord
from discord.ext import commands
from core.classes import Cog_Extension
from cmds.music import Music
import json
import datetime

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["channel"]))
        await channel.send(f"{member} join!")
        print(f"{datetime.datetime.now()} {member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["channel"]))
        await channel.send(f"{member} leave!")
        print(f"{datetime.datetime.now()} {member} leave!")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("hi") and msg.author != self.bot.user:
            await msg.channel.send(f"{msg.author.mention} hi")
            print(f"{datetime.datetime.now()} {msg.author.mention} hi")

        if msg.content.endswith("bye") and msg.author != self.bot.user:
            await msg.channel.send(f"{msg.author.mention} bye")
            print(f"{datetime.datetime.now()} {msg.author.mention} bye")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if not hasattr(ctx.commands, "on_error"):

            if isinstance(error, commands.errors.MissingRequiredArgument):
                await ctx.send("Missing argument(s)")
            elif isinstance(error, commands.errors.CommandNotFound):
                await ctx.send("Command not found")
            elif isinstance(error, commands.errors.TooManyArguments):
                await ctx.send("Too many Arguments")
            elif isinstance(error, commands.errors.UserInputError):
                await ctx.send("Wrong type of input(s)")
            else:
                await ctx.send(f"Error: {error}")

            print(f"{datetime.datetime.now()} error: {error}")

    @Music.play.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("URL is missing")
            print(f"{datetime.datetime.now()} play music missing url")
        elif isinstance(error, commands.errors.TooManyArguments):
            await ctx.send("Only one url will be accepted")
            print(f"{datetime.datetime.now} play music input more than one args")


def setup(bot):
    bot.add_cog(Event(bot))
