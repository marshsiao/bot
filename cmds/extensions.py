import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import time

def nowtime():
    sec = time.time()
    now = time.localtime(sec)
    str = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour+8}:{now.tm_min}:{now.tm_sec} UTC+8")
    return str

class extensions(Cog_Extension):
    #骰子
    @commands.slash_command(name = '骰子', description = '骰骰子')
    async def dice(self,ctx):
        dicenum = random.randint(1,6)
        print(f"dice used at {nowtime()}")
        if dicenum == 1:
            await ctx.respond(file = discord.File('image/dice1.png'))
        if dicenum == 2:
            await ctx.respond(file = discord.File('image/dice2.png'))
        if dicenum == 3:
            await ctx.respond(file = discord.File('image/dice3.png'))
        if dicenum == 4:
            await ctx.respond(file = discord.File('image/dice4.png'))
        if dicenum == 5:
            await ctx.respond(file = discord.File('image/dice5.png'))
        if dicenum == 6:
            await ctx.respond(file = discord.File('image/dice6.png'))

    #猜拳
    @commands.slash_command(name = '猜拳', description = '跟好友來猜拳吧')
    async def paper_scissors(self,ctx):
        rand = random.randint(1,3)
        print(f"paper_scissors used at {nowtime()}")
        if rand == 1:
            await ctx.respond(file = discord.File('image/paper.png'))
        if rand == 2:
            await ctx.respond(file = discord.File('image/scissors.png'))
        if rand == 3:
            await ctx.respond(file = discord.File('image/stone.png'))
            
    #選路
    @commands.slash_command(name = '選路')
    async def pick_lane(self,ctx):
        dicenum = random.randint(1,5)
        print(f"pick_lane used at {nowtime()}")
        if dicenum == 1:
            embed = discord.Embed(title = '選路', description = '乖乖去上路', colour = discord.Colour.blue())
            await ctx.respond(embed = embed)
        if dicenum == 2:
            embed = discord.Embed(title = '選路', description = '乖乖去打野', colour = discord.Colour.blue())
            await ctx.respond(embed = embed)
        if dicenum == 3:
            embed = discord.Embed(title = '選路', description = '乖乖去中路', colour = discord.Colour.blue())
            await ctx.respond(embed = embed)
        if dicenum == 4:
            embed = discord.Embed(title = '選路', description = '乖乖去下路', colour = discord.Colour.blue())
            await ctx.respond(embed = embed)
        if dicenum == 5:
            embed = discord.Embed(title = '選路', description = '乖乖去輔助', colour = discord.Colour.blue())
            await ctx.respond(embed = embed)
    

def setup(bot):
    bot.add_cog(extensions(bot))