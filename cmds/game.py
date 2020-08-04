import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randrange
from asyncio import run

class Game(Cog_Extension):
    game_map = []
    char_ran_cor = 0
    ball_ran_cor = 0
    targ_ran_cor = 0

    @commands.command()
    async def game(self, ctx):
        self.game_map.clear() 

        self.char_ran_cor = randrange(0, 28)
        self.ball_ran_cor = randrange(8, 20)
        self.targ_ran_cor = randrange(0, 28)
        while self.ball_ran_cor == self.char_ran_cor or (self.ball_ran_cor) % 7 == 0 or (self.ball_ran_cor) % 7 == 6:
            self.ball_ran_cor = randrange(8, 20)
        while self.targ_ran_cor == self.char_ran_cor or self.targ_ran_cor == self.ball_ran_cor:
            self.targ_ran_cor = randrange(0, 28)

        for i in range(28):
            if i == self.char_ran_cor and i != self.ball_ran_cor and i != self.targ_ran_cor:
                self.game_map.append(":smiley:")
            elif i == self.ball_ran_cor and i != self.char_ran_cor and i != self.targ_ran_cor:
                self.game_map.append(":basketball:")
            elif i == self.targ_ran_cor and i != self.char_ran_cor and i != self.ball_ran_cor:
                self.game_map.append(":nazar_amulet:")
            else:
                self.game_map.append(":white_large_square:")

        await self.print_game(ctx)
            

    @commands.command()
    async def w(self, ctx):
        if self.char_ran_cor > 6 and not(self.char_ran_cor-7 == self.ball_ran_cor and self.ball_ran_cor < 7) and self.char_ran_cor-7 != self.targ_ran_cor:
            self.game_map[self.char_ran_cor] = ":white_large_square:"
            self.game_map[self.char_ran_cor-7] = ":smiley:"
            self.char_ran_cor -= 7

        if self.char_ran_cor == self.ball_ran_cor:
            self.game_map[self.ball_ran_cor-7] = ":basketball:"
            self.ball_ran_cor -= 7

        await self.print_game(ctx)
    
    @commands.command()
    async def a(self, ctx):
        if self.char_ran_cor%7 != 0 and not(self.char_ran_cor-1 == self.ball_ran_cor and self.ball_ran_cor % 7 == 0) and self.char_ran_cor-1 != self.targ_ran_cor:
            self.game_map[self.char_ran_cor] = ":white_large_square:"
            self.game_map[self.char_ran_cor-1] = ":smiley:"
            self.char_ran_cor -= 1

        if self.char_ran_cor == self.ball_ran_cor:
            self.game_map[self.ball_ran_cor-1] = ":basketball:"
            self.ball_ran_cor -= 1

        await self.print_game(ctx)
        
    @commands.command()
    async def s(self, ctx):
        if self.char_ran_cor < 21 and not(self.char_ran_cor+7 == self.ball_ran_cor and self.ball_ran_cor > 20) and self.char_ran_cor+7 != self.targ_ran_cor:
            self.game_map[self.char_ran_cor] = ":white_large_square:"
            self.game_map[self.char_ran_cor+7] = ":smiley:"
            self.char_ran_cor += 7

        if self.char_ran_cor == self.ball_ran_cor:
            self.game_map[self.ball_ran_cor+7] = ":basketball:"
            self.ball_ran_cor += 7

        await self.print_game(ctx)

    @commands.command()
    async def d(self, ctx):
        if self.char_ran_cor%7 != 6 and not(self.char_ran_cor+1 == self.ball_ran_cor and self.ball_ran_cor % 7 == 6) and self.char_ran_cor+1 != self.targ_ran_cor:
            self.game_map[self.char_ran_cor] = ":white_large_square:"
            self.game_map[self.char_ran_cor+1] = ":smiley:"
            self.char_ran_cor += 1

        if self.char_ran_cor == self.ball_ran_cor:
            self.game_map[self.ball_ran_cor+1] = ":basketball:"
            self.ball_ran_cor += 1
        
        await self.print_game(ctx)

    async def print_game(self, ctx):
        if self.ball_ran_cor == self.targ_ran_cor:
            self.game_map[self.targ_ran_cor] = ":rosette:"

        game_row = ":red_square:"*9 + "\n"
        for i in range(4):
            game_row += ":red_square:"
            for j in range(7):
                game_row = game_row + Game.game_map[(i*7)+j]
            game_row = game_row+":red_square:\n"
            
        game_row += ":red_square:"*9
        embed = discord.Embed(title="Level 1", description = game_row, color = 0x00e1ff)
        await ctx.send(embed=embed)

        if self.ball_ran_cor == self.targ_ran_cor:
            await ctx.send("Congratulations! you win level 1\nType the game command to restart the game")
        

def setup(bot): 
    bot.add_cog(Game(bot))