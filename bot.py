import discord
import json
from discord.ext import commands
from core.classes import database
import os

with open('setting.json', mode = 'r', encoding = 'utf8')as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix = '~', help_command = None)
owner_id = '398833628978872320'


#啟動訊息
@bot.event
async def on_ready():
    print('<login>')
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = '/help /公告'))

#加入伺服器新建setting
@bot.event
async def on_guild_join(guild):
    guild_id = guild.id
    database.create_initdata(guild_id)

#離開伺服器刪除setting
@bot.event
async def on_guild_remove(guild):
    guild_id = guild.id
    database.drop_table(guild_id)
    database.drop_saystable(guild_id)

#指令錯誤
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        embed_error = discord.Embed(title = '警告', description = '**指令錯誤請輸入** `~help` **來確認指令列表**', colour = discord.Colour.red())
        await ctx.send(embed = embed_error)
    if isinstance(error, commands.MissingPermissions):
        embed_error = discord.Embed(title = '警告', description = '**你沒有使用此指令的權限**', colour = discord.Colour.red())
        await ctx.send(embed = embed_error)

#reload extension
@bot.slash_command(guild_ids = [862311936322306068],name = 'reload')
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    embed = discord.Embed(title = 'Reload', colour = discord.Colour.blue())
    embed.add_field(name = '\u200B', value = f'extension `{extension}` reloaded!', inline = False)
    await ctx.respond(embed = embed)
    

#load extension
@bot.slash_command(guild_ids = [862311936322306068],name = 'load')
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    embed = discord.Embed(title = 'Load', colour = discord.Colour.blue())
    embed.add_field(name = '\u200B', value = f'extension `{extension}` reloaded!', inline = False)
    await ctx.respond(embed = embed)
   

#unload extension
@bot.slash_command(guild_ids = [862311936322306068],name = 'unload')
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    embed = discord.Embed(title = 'Unload', colour = discord.Colour.blue())
    embed.add_field(name = '\u200B', value = f'extension `{extension}` reloaded!', inline = False)
    await ctx.respond(embed = embed)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['Token'])