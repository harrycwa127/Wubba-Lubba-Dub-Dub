import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randrange


class Game(Cog_Extension):
    lv = 1
    game_map = []
    char_ran_cor = 0
    ball_ran_cor = []
    targ_ran_cor = []
    cell_col = 6 + lv
    cell_num = cell_col * (3 + lv)


    @commands.command()
    async def game(self, ctx):
        self.game_map.clear()
        self.ball_ran_cor.clear()
        self.targ_ran_cor.clear()

        self.char_ran_cor = randrange(0, self.cell_num)
        for i in range(self.lv):
            temp = randrange((self.cell_col + 1), self.cell_num - self.cell_col - 1)
            while (
                temp == self.char_ran_cor
                or temp % self.cell_col == 0
                or temp % self.cell_col == (self.cell_col - 1)
                or temp in self.ball_ran_cor
            ):
                temp = randrange((self.cell_col + 1), self.cell_num - self.cell_col - 1)
            self.ball_ran_cor.append(temp)

            temp = randrange(0, self.cell_num)
            while (
                temp == self.char_ran_cor
                or temp in self.ball_ran_cor
                or temp in self.targ_ran_cor
            ):
                temp = randrange(0, self.cell_num)
            self.targ_ran_cor.append(temp)

        for i in range(self.cell_num):
            if i == self.char_ran_cor:
                self.game_map.append(":smiley:")
            elif i in self.ball_ran_cor:
                self.game_map.append(":basketball:")
            elif i in self.targ_ran_cor:
                self.game_map.append(":nazar_amulet:")
            else:
                self.game_map.append(":white_large_square:")

        await self.print_game(ctx)


    @commands.command()
    async def w(self, ctx):
        if (
            self.char_ran_cor >= self.cell_col
            and not (
                (self.char_ran_cor - self.cell_col) in self.ball_ran_cor
                and (self.char_ran_cor - self.cell_col) < self.cell_col
            )
            and not (self.char_ran_cor - self.cell_col) in self.targ_ran_cor
        ):
            self.game_map[self.char_ran_cor] = ":white_large_square:"
            self.game_map[self.char_ran_cor - self.cell_col] = ":smiley:"
            self.char_ran_cor -= self.cell_col

        if self.char_ran_cor in self.ball_ran_cor:
            self.game_map[
                self.char_ran_cor - self.cell_col
            ] = ":basketball:"
            self.ball_ran_cor[self.ball_ran_cor.index(self.char_ran_cor)] -= self.cell_col
            await self.detect_targ(self.char_ran_cor - self.cell_col)

        await self.print_game(ctx)


    @commands.command()
    async def a(self, ctx):
        if (
            self.char_ran_cor % self.cell_col != 0
            and not (
                (self.char_ran_cor - 1) in self.ball_ran_cor
                and (self.char_ran_cor -1) % self.cell_col == 0
            )
            and not (self.char_ran_cor - 1) in self.targ_ran_cor
        ):
            self.game_map[self.char_ran_cor] = ":white_large_square:"
            self.game_map[self.char_ran_cor - 1] = ":smiley:"
            self.char_ran_cor -= 1

        if self.char_ran_cor in self.ball_ran_cor:
            self.game_map[self.char_ran_cor - 1] = ":basketball:"
            self.ball_ran_cor[self.ball_ran_cor.index(self.char_ran_cor)] -= 1
            await self.detect_targ(self.char_ran_cor - 1)

        await self.print_game(ctx)


    @commands.command()
    async def s(self, ctx):
        if (
            self.char_ran_cor < (self.cell_num-self.cell_col)
            and not (
                (self.char_ran_cor + self.cell_col) in self.ball_ran_cor
                and (self.char_ran_cor + self.cell_col) >= (self.cell_num-self.cell_col)
            )
            and not (self.char_ran_cor + self.cell_col) in self.targ_ran_cor
        ):
            self.game_map[self.char_ran_cor] = ":white_large_square:"
            self.game_map[self.char_ran_cor + self.cell_col] = ":smiley:"
            self.char_ran_cor += self.cell_col

        if self.char_ran_cor in self.ball_ran_cor:
            self.game_map[
                self.char_ran_cor + self.cell_col
            ] = ":basketball:"
            self.ball_ran_cor[self.ball_ran_cor.index(self.char_ran_cor)] += self.cell_col
            await self.detect_targ(self.char_ran_cor + self.cell_col)

        await self.print_game(ctx)


    @commands.command()
    async def d(self, ctx):
        if (
            self.char_ran_cor % self.cell_col != (self.cell_col-1)
            and not (
                (self.char_ran_cor + 1) in self.ball_ran_cor
                and (self.char_ran_cor + 1) % self.cell_col == (self.cell_col-1)
            )
            and not (self.char_ran_cor + 1) in self.targ_ran_cor
        ):
            self.game_map[self.char_ran_cor] = ":white_large_square:"
            self.game_map[self.char_ran_cor + 1] = ":smiley:"
            self.char_ran_cor += 1

        if self.char_ran_cor in self.ball_ran_cor:
            self.game_map[self.char_ran_cor + 1] = ":basketball:"
            self.ball_ran_cor[self.ball_ran_cor.index(self.char_ran_cor)] += 1
            await self.detect_targ(self.char_ran_cor + 1) 

        await self.print_game(ctx)


    async def detect_targ(self, ball):
        if ball in self.targ_ran_cor:
            self.game_map[ball] = ":rosette:"


    async def print_game(self, ctx):

        game_row = ":red_square:" * (8 + self.lv) + "\n"
        for i in range(3 + self.lv):
            game_row += ":red_square:"
            for j in range(6 + self.lv):
                game_row = game_row + self.game_map[i * (6 + self.lv) + j]
            game_row += ":red_square:\n"

        game_row += ":red_square:" * (8 + self.lv)
        embed = discord.Embed(
            title=f"Level {self.lv}", description=game_row, color=0x00E1FF
        )

        win = True
        for j in self.targ_ran_cor:
            if self.game_map[j] != ":rosette:":
                win = False
        if win:
            embed.add_field(name=f"Congratulations! you win level {self.lv}", value="Type the game command to restart the game")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Game(bot))
