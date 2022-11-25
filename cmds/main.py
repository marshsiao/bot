from discord.ext.commands import MissingPermissions
from discord import Member
from discord.commands import Option
import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
from core.classes import data_parse
import time

def nowtime():
    sec = time.time()
    now = time.localtime(sec)
    str = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour+8}:{now.tm_min}:{now.tm_sec} UTC+8")
    return str
    

class main(Cog_Extension):
    #機器人延遲 bot latency
    @commands.slash_command(name = 'ping', description = '機器人和用戶的延遲')
    async def ping(self,ctx):
        embed_ping = discord.Embed(title = '延遲',colour = discord.Colour.blue())
        embed_ping.add_field(name = '機器人延遲(毫秒)', value = f'`{round(self.bot.latency*1000)}` ms', inline = False)
        await ctx.respond(embed = embed_ping)
        print(f"ping used at {nowtime()}")
    
    #機器人公告
    @commands.slash_command(name = '公告', description = '最新公告')
    async def post(self,ctx):
        with open('changelog.json', mode = 'r', encoding = 'utf8')as jf:
            jopen = json.load(jf)
        embed = discord.Embed(title = '公告', description = '機器人狀態: 所有功能正常', colour = discord.Colour.blue())
        embed.add_field(name = '(9/8) 更新內容', value = ('新功能:斜線指令' +'\n' + jopen['1']), inline = True)
        embed.add_field(name = '其他更新內容', value = (jopen['2']), inline = True)
        await ctx.respond(embed = embed)
        print(f"post used at {nowtime()}")
    
    #settings 伺服器設定檔
    '''@commands.slash_command(name = 'settings', description = '伺服器設定檔')
    @commands.has_permissions(administrator = True, manage_guild = True)
    async def settings(self, ctx, 設定: Option(str, '想改變的設定', required = False, default = ''),
                                  值: Option(str, 'true/false', required = False, default = '')):
        setting = 設定
        value = 值
        guild_id = str(ctx.guild.id)
        try:
            view_data = database.view_data(guild_id)
            if view_data == []:
                database.create_initdata(guild_id)
                view_data = database.view_data(guild_id)
                embed_setting = discord.Embed(title = 'Settings', colour = discord.Colour.blue())
                embed_setting.add_field(name = 'acct_id', value = database.select_data(guild_id,'acct_id'), inline = True)
                embed_setting.add_field(name = 'lol_search_all_id', value = database.select_data(guild_id,'lol_search_all_id'), inline = True)
                embed_setting.add_field(name = 'server_management', value = database.select_data(guild_id,'server_management'), inline = True)
                embed_setting.add_field(name = 'quotations', value = database.select_data(guild_id,'quotations'), inline = True)
                embed_setting.set_footer(text = '改變設定檔格式(/settings 想改變的設定 值(true/false))')
                await ctx.respond(embed = embed_setting)
            else:
                if (setting == '' and  value == ''):
                    view_data = database.view_data(guild_id)
                    embed_setting = discord.Embed(title = 'Settings', colour = discord.Colour.blue())
                    embed_setting.add_field(name = 'acct_id', value = database.select_data(guild_id,'acct_id'), inline = True)
                    embed_setting.add_field(name = 'lol_search_all_id', value = database.select_data(guild_id,'lol_search_all_id'), inline = True)
                    embed_setting.set_footer(text = '改變設定檔格式(/settings 想改變的設定 值(true/false))')
                    await ctx.respond(embed = embed_setting)
                elif ((value == 'true' or value == 'false') 
                    and (setting == 'acct_id' or setting == 'server_management' or setting == 'lol_search_all_id' or setting == 'quotations')):
                    database.update_data(guild_id, setting, value)
                    view_data = database.view_data(guild_id)
                    embed_setting = discord.Embed(title = 'Settings', colour = discord.Colour.blue())
                    embed_setting.add_field(name = 'acct_id', value = database.select_data(guild_id,'acct_id'), inline = True)
                    embed_setting.add_field(name = 'lol_search_all_id', value = database.select_data(guild_id,'lol_search_all_id'), inline = True)
                    embed_setting.set_footer(text = '改變設定檔格式(//settings 想改變的設定 值(true/false))')
                    await ctx.respond(embed = embed_setting)
                else:
                    await ctx.respond('錯誤的 `設定` 或 `值`')
        except:
            embed_setting = discord.Embed(title = 'Settings', description = '資料庫維修中請稍後再嘗試', colour = discord.Colour.blue())
            await ctx.respond(embed = embed_setting)'''
            
            
def setup(bot):
    bot.add_cog(main(bot))