import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randrange
import datetime
import json

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Game(Cog_Extension):
    lv = 1
    game_map = []
    char_ran_cor = 0
    ball_ran_cor = []
    targ_ran_cor = []
    cell_col = 0
    cell_num = 0
    bg = ":fog:"
    ball = ":basketball:"
    frame = ":red_square:"
    player = ":smiley:"
    targ = ":nazar_amulet:"
    targ_fin = ":rosette:"


    @commands.command()
    async def game(self, ctx):
        self.game_map.clear()
        self.ball_ran_cor.clear()
        self.targ_ran_cor.clear()
        self.cell_col = 6 + self.lv
        self.cell_num = self.cell_col * (3 + self.lv)
        print(f"{datetime.datetime.now()} start game with lv{self.lv}")

        self.char_ran_cor = randrange(0, self.cell_num)
        for i in range(self.lv):
            count_ball = 0
            count_targ = 0
            temp = randrange((self.cell_col + 1), self.cell_num - self.cell_col - 1)

            for i in range(-self.cell_col, self.cell_col, self.cell_col):
                for j in range(-1, 1, 1):
                    if (temp + i + j) in self.ball_ran_cor:
                        count_ball += 1
                        
            while (
                temp == self.char_ran_cor
                or temp % self.cell_col == 0
                or temp % self.cell_col == (self.cell_col - 1)
                or temp in self.ball_ran_cor
                or count_ball > 2
            ):
                temp = randrange((self.cell_col + 1), self.cell_num - self.cell_col - 1)
            self.ball_ran_cor.append(temp)

            temp = randrange(0, self.cell_num)

            for i in range(-self.cell_col, self.cell_col, self.cell_col):
                for j in range(-1, 1, 1):
                    if (temp + i + j) in self.targ_ran_cor:
                        count_targ += 1

            while (
                temp == self.char_ran_cor
                or temp in self.ball_ran_cor
                or temp in self.targ_ran_cor
                or count_targ > 3
            ):
                temp = randrange(0, self.cell_num)
            self.targ_ran_cor.append(temp)

        for i in range(self.cell_num):
            if i == self.char_ran_cor:
                self.game_map.append(self.player)
            elif i in self.ball_ran_cor:
                self.game_map.append(self.ball)
            elif i in self.targ_ran_cor:
                self.game_map.append(self.targ)
            else:
                self.game_map.append(self.bg)

        await self.print_game(ctx)


    @commands.Cog.listener()
    async def on_message(self, msg):
        channel = self.bot.get_channel(jdata["channel"])
        if msg.content == "w" and msg.channel == channel:
            await self.w(channel)
        elif msg.content == "a" and msg.channel == channel:
            await self.a(channel)
        elif msg.content == "s" and msg.channel == channel:
            await self.s(channel)
        elif msg.content == "d" and msg.channel == channel:
            await self.d(channel)


    async def w(self, ctx):
        if (
            self.char_ran_cor >= self.cell_col
            and not (
                self.game_map[(self.char_ran_cor - self.cell_col)] == self.ball
                and (
                    (self.char_ran_cor - self.cell_col) < self.cell_col
                    or self.game_map[(self.char_ran_cor - self.cell_col - self.cell_col)] == self.ball
                    or self.game_map[(self.char_ran_cor - self.cell_col - self.cell_col)] == self.targ_fin
                )
            )
            and not (self.char_ran_cor - self.cell_col) in self.targ_ran_cor 
        ):
            self.game_map[self.char_ran_cor] = self.bg
            self.game_map[self.char_ran_cor - self.cell_col] = self.player
            self.char_ran_cor -= self.cell_col

        if self.char_ran_cor in self.ball_ran_cor:
            self.game_map[
                self.char_ran_cor - self.cell_col
            ] = self.ball
            self.ball_ran_cor[self.ball_ran_cor.index(self.char_ran_cor)] -= self.cell_col
            await self.detect_targ(self.char_ran_cor - self.cell_col)

        await self.print_game(ctx)


    async def a(self, ctx):
        if (
            self.char_ran_cor % self.cell_col != 0
            and not (
                (self.char_ran_cor - 1) in self.ball_ran_cor
                and(
                    (self.char_ran_cor -1) % self.cell_col == 0
                    or self.game_map[(self.char_ran_cor - 2)] == self.ball
                    or self.game_map[(self.char_ran_cor - 2)] == self.targ_fin
                ) 
            )
            and not (self.char_ran_cor - 1) in self.targ_ran_cor
        ):
            self.game_map[self.char_ran_cor] = self.bg
            self.game_map[self.char_ran_cor - 1] = self.player
            self.char_ran_cor -= 1

        if self.char_ran_cor in self.ball_ran_cor:
            self.game_map[self.char_ran_cor - 1] = self.ball
            self.ball_ran_cor[self.ball_ran_cor.index(self.char_ran_cor)] -= 1
            await self.detect_targ(self.char_ran_cor - 1)

        await self.print_game(ctx)


    async def s(self, ctx):
        if (
            self.char_ran_cor < (self.cell_num-self.cell_col)
            and not (
                (self.char_ran_cor + self.cell_col) in self.ball_ran_cor
                and(
                    (self.char_ran_cor + self.cell_col) >= (self.cell_num-self.cell_col)
                    or self.game_map[(self.char_ran_cor + self.cell_col + self.cell_col)] == self.ball
                    or self.game_map[(self.char_ran_cor + self.cell_col + self.cell_col)] == self.targ_fin 
                ) 
            )
            and not (self.char_ran_cor + self.cell_col) in self.targ_ran_cor
        ):
            self.game_map[self.char_ran_cor] = self.bg
            self.game_map[self.char_ran_cor + self.cell_col] = self.player
            self.char_ran_cor += self.cell_col

        if self.char_ran_cor in self.ball_ran_cor:
            self.game_map[
                self.char_ran_cor + self.cell_col
            ] = self.ball
            self.ball_ran_cor[self.ball_ran_cor.index(self.char_ran_cor)] += self.cell_col
            await self.detect_targ(self.char_ran_cor + self.cell_col)

        await self.print_game(ctx)


    async def d(self, ctx):
        if (
            self.char_ran_cor % self.cell_col != (self.cell_col-1)
            and not (
                (self.char_ran_cor + 1) in self.ball_ran_cor
                and(
                    (self.char_ran_cor + 1) % self.cell_col == (self.cell_col-1)
                    or self.game_map[(self.char_ran_cor + 2)] == self.ball
                    or self.game_map[(self.char_ran_cor + 2)] == self.targ_fin
                )
            )
            and not (self.char_ran_cor + 1) in self.targ_ran_cor
        ):
            self.game_map[self.char_ran_cor] = self.bg
            self.game_map[self.char_ran_cor + 1] = self.player
            self.char_ran_cor += 1

        if self.char_ran_cor in self.ball_ran_cor:
            self.game_map[self.char_ran_cor + 1] = self.ball
            self.ball_ran_cor[self.ball_ran_cor.index(self.char_ran_cor)] += 1
            await self.detect_targ(self.char_ran_cor + 1) 

        await self.print_game(ctx)


    async def detect_targ(self, ball):
        if ball in self.targ_ran_cor:
            self.game_map[ball] = self.targ_fin

    
    @commands.command()
    async def reset(self, ctx):
        self.lv = 1
        await self.game(ctx)
        print(f"{datetime.datetime.now()} reset game")
    

    @commands.command()
    async def set_lv(self, ctx, lv:int):
        if lv < 8:
            self.lv = lv
            await self.game(ctx)
            print(f"{datetime.datetime.now()} set level to lv{lv}")
        else:
            await ctx.send("The maximum level of the game is 7")


    @commands.command()
    async def print_game(self, ctx):
        game_row = self.frame * (8 + self.lv) + "\n"
        for i in range(3 + self.lv):
            game_row += self.frame
            for j in range(6 + self.lv):
                game_row = game_row + self.game_map[i * (6 + self.lv) + j]
            game_row += self.frame + "\n"

        game_row += ":red_square:" * (8 + self.lv)
        embed = discord.Embed(
            title=f"Level {self.lv}", description=game_row, color=0x00E1FF
        )

        win = True
        for j in self.targ_ran_cor:
            if self.game_map[j] != self.targ_fin:
                win = False
        if win:
            embed.add_field(name=f"Congratulations! you win level {self.lv}", value="Type the game command to restart the game in same level, type reset command to reset level")
            print(f"{datetime.datetime.now()} game pass lv{self.lv}")
        await ctx.send(embed=embed)

        if win:
            if self.lv < 7:
                self.lv += 1
            else:
                await ctx.send("The maximum level of the game is 7")

            await self.game(ctx)
        



def setup(bot):
    bot.add_cog(Game(bot))
