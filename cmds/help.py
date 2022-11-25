from core.classes import Cog_Extension
from core.classes import database
from core.classes import data_parse
from discord.ext import commands
from discord.commands import Option
import discord
import time

def nowtime():
    sec = time.time()
    now = time.localtime(sec)
    str = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour+8}:{now.tm_min}:{now.tm_sec} UTC+8")
    return str

owner_id = '398833628978872320'

class help(Cog_Extension):
    #help指令
    @commands.slash_command(name = 'help', description = '指令列表')
    async def help(self,ctx, 指令: Option(str,'help', required = False, default = '')):
        command = 指令
        if command == '':
            main_func = ['/骰子', '/猜拳', '/ping']
            lol_func = ['/查玩家', '/查英雄', '/選路']
            #permission_required_func = ['/settings']
            embed_help = discord.Embed(title = "指令", description = '指令功能說明 /help `(指令)`',colour = discord.Colour.blue())
            embed_help.add_field(name = '基本功能', value = data_parse.create_string(main_func), inline = True)
            embed_help.add_field(name = 'LOL功能', value = data_parse.create_string(lol_func), inline = True)
            await ctx.respond(embed = embed_help)
            print(f'help used at {nowtime()}')
        elif command == '查玩家':
            embed_help = discord.Embed(title = "查玩家",colour = discord.Colour.blue())
            embed_help.add_field(name = '功能描述', value = '/查玩家 [`玩家名稱`]' + '\nLOL玩家查詢 顯示過去ID 過去牌位', inline = True)
            await ctx.respond(embed = embed_help)
        elif command == '查英雄':
            embed_help = discord.Embed(title = "查英雄",description = '',colour = discord.Colour.blue())
            embed_help.add_field(name = '功能指令範例', value = '/查英雄 [`英雄名稱`] (中/英) 皆可以查詢' + '\n/查英雄 [`英雄名稱`] [`路線`] 可指定想要查詢的英雄在特定路線上的數據', inline = True)
            await ctx.respond(embed = embed_help)
        elif command == 'ping':
            embed_help = discord.Embed(title = "ping",colour = discord.Colour.blue())
            embed_help.add_field(name = '功能描述', value = '機器人延遲', inline = True)
            await ctx.respond(embed = embed_help)
        else:
            embed_help = discord.Embed(title = "指令",colour = discord.Colour.red())
            embed_help.add_field(name = '\u200B', value = f'**此指令 `{command}` 沒有說明**', inline = True)
            await ctx.respond(embed = embed_help)            
            
        '''elif command == 'settings':
            embed_help = discord.Embed(title = "settings",description = '設定檔功能 (true(開啟)/false(關閉))',colour = discord.Colour.blue())
            embed_help.add_field(name = '`acct_id`', value = '預設false 開啟為 LOL玩家查詢顯示GarenaID', inline = True)
            embed_help.add_field(name = '`lol_search_all_id`', value = '預設false 開啟為 LOL玩家查詢 顯示所有過去ID', inline = True)
            await ctx.respond(embed = embed_help)'''
            
def setup(bot):
    bot.add_cog(help(bot))