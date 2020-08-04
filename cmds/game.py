import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Game(Cog_Extension):
    game_map = [4*7]

    @commands.command()
    async def game(self, ctx):
        # await ctx.send(f"{':red_square:'*9}")

        # char_ran_row = random.randrange(0, 4)
        # char_ran_col = random.randrange(0, 7)
        # ball_ran_row = random.randrange(1, 3)
        # ball_ran_col = random.randrange(1, 6)
        # while ball_ran_col == char_ran_col and ball_ran_row == char_ran_row:
        #     ball_ran_row = random.randrange(0, 4)
        #     ball_ran_col = random.randrange(0, 7)
        
        # for i in range(4):
        #     if i != char_ran_row and i != ball_ran_row:
        #         await ctx.send(f"{':red_square:'+':white_large_square:'*7+':red_square:'}")
        #     elif i == char_ran_row and i != ball_ran_row:
        #         await ctx.send(f"{':red_square:'+':white_large_square:'*char_ran_col+':smiley:'+':white_large_square:'*(7-char_ran_col-1)+':red_square:'}")
        #     elif i == ball_ran_row and i != char_ran_row:
        #         await ctx.send(f"{':red_square:'+':white_large_square:'*ball_ran_col+':basketball:'+':white_large_square:'*(7-ball_ran_col-1)+':red_square:'}")
        #     elif i == ball_ran_row and i == char_ran_row:
        #         if ball_ran_col < char_ran_col:
        #             await ctx.send(f"{':red_square:'+':white_large_square:'*ball_ran_col+':basketball:'+':white_large_square:'*(char_ran_col-ball_ran_col-1)+':smiley:'+':white_large_square:'*(7-char_ran_col-1)+':red_square:'}")
        #         elif char_ran_col < ball_ran_col:
        #             await ctx.send(f"{':red_square:'+':white_large_square:'*char_ran_col+':smiley:'+':white_large_square:'*(ball_ran_col-char_ran_col-1)+':basketball:'+':white_large_square:'*(7-ball_ran_col-1)+':red_square:'}")

        # await ctx.send(f"{':red_square:'*9}")

        char_ran_cor = random.randrange(0, 28)
        ball_ran_cor = random.randrange(1, 27)
        while ball_ran_cor == char_ran_cor or (ball_ran_cor+1) % 7 == 0 or (ball_ran_cor+1) % 7 == 1:
            ball_ran_cor = random.randrange(1, 27)
        for i in range(28):
            if i == char_ran_cor and i != ball_ran_cor:
                Game.game_map[i] = ":smiley:"
            elif i == ball_ran_cor and i != char_ran_cor:
                Game.game_map[i] = ":basketball:"
            else:
                Game.game_map[i] = ":white_large_square:" 

        await ctx.send(f"{':red_square:'*9}")

        for i in range(4):
            game_row = ":red_square:"
            for j in range(1, 8):
                game_row = game_row + Game.game_map[i*j-1]
            game_row = game_row+":red_square:"
            await ctx.send(game_row)

        await ctx.send(f"{':red_square:'*9}")


def setup(bot):
    bot.add_cog(Game(bot))