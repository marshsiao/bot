import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core.classes import data_parse
from discord.commands import Option
from bs4 import BeautifulSoup 
import cloudscraper
import time

def nowtime():
    sec = time.time()
    now = time.localtime(sec)
    str = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour+8}:{now.tm_min}:{now.tm_sec} UTC+8")
    return str

class lol_search(Cog_Extension):
    #LOL 玩家查詢
    @commands.slash_command(name = '查玩家', description = '英雄聯盟玩家查詢')
    async def search(self, ctx, 玩家名稱: Option(str,'玩家名稱', required = True, default = '')):
        title_list = ['S3牌位: ','S4牌位: ','S5牌位: ','S6牌位: ','S7牌位: ','S8牌位: ','S9牌位: ','S10牌位:']
        id = 玩家名稱
        if id == '':
            embed_lol = discord.Embed(title = '錯誤', description = '**請輸入想查詢之玩家名稱**', colour = discord.Colour.red())
            await ctx.respond(embed = embed_lol)
        else:
            scraper = cloudscraper.create_scraper()
            response = scraper.get(f'https://lol.moa.tw/summoner/show/{id}')
            soup = BeautifulSoup(response.text,"html.parser")
            find_id = soup.find('dl' , class_="dl-horizontal prevname h3")
            find_rk = soup.find('dl' , class_="dl-horizontal sub-jumbotron h3")
            find_time = soup.find('div' , class_="label label-info pull-left personalfile-last-update")
            try:
                find_lv = soup.find_all('div', class_='col-xs-12')
                imgdata = soup.find_all('img')
                lv_id = find_lv[3].text.split(' ')
                sel_rk = find_rk.select('dd')
                list_rk = data_parse.translate(sel_rk)
                if find_id == None:
                    embed_lol = discord.Embed(title = lv_id[1] + ' ' + id.replace('%20',' '), colour = discord.Colour.blue())
                    embed_lol.add_field(name = '過去牌位', value = data_parse.list_zip_2(title_list,list_rk), inline = True)
                    embed_lol.add_field(name = '過去召喚師名稱', value = '無過去召喚師名稱', inline = True)
                    embed_lol.set_thumbnail(url = data_parse.img_list(imgdata)[0])
                    embed_lol.set_footer(text = f"此機器人已在 {len(self.bot.guilds)} 個伺服器中服務" + '\n' + '原始資料來自: https://lol.moa.tw/' + '\n' + find_time.text.replace('Last Modified date','最後更新日期'))
                    await ctx.respond(embed = embed_lol)
                    print(f'lol search at {nowtime()} response code : {response.status_code}')
                else:
                    sel_id = find_id.select('dt')
                    sel_id_time = find_id.select('dd')
                    id_time = data_parse.create_string_2(sel_id_time).split(' ')
                    id_time = id_time[0: len(id_time)-1: 2]
                    if len(sel_id) <= 10:
                        embed_lol = discord.Embed(title = lv_id[1] + ' ' + id.replace('%20',' '), colour = discord.Colour.blue())
                        embed_lol.add_field(name = '過去牌位', value = data_parse.list_zip_2(title_list,list_rk), inline = True)
                        embed_lol.add_field(name = '過去召喚師名稱', value = data_parse.list_zip(id_time,sel_id), inline = True)
                        embed_lol.set_thumbnail(url = data_parse.img_list(imgdata)[0])
                        embed_lol.set_footer(text = f"此機器人已在 {len(self.bot.guilds)} 個伺服器中服務" + '\n' + '原始資料來自: https://lol.moa.tw/' + '\n' + find_time.text.replace('Last Modified date','最後更新日期'))
                        await ctx.respond(embed = embed_lol)
                        print(f'lol search at {nowtime()} response code : {response.status_code}')
                    elif len(sel_id) > 10:
                        list_id = list(data_parse.cutlist(sel_id))
                        id_time = list(data_parse.cutlist_2(id_time))
                        embed_lol = discord.Embed(title = lv_id[1] + ' ' + id.replace('%20',' '), colour = discord.Colour.blue())
                        embed_lol.add_field(name = '過去牌位', value = data_parse.list_zip_2(title_list,list_rk), inline = True)
                        embed_lol.add_field(name = '過去召喚師名稱', value = data_parse.list_zip_2(id_time,list_id), inline = True)
                        embed_lol.set_thumbnail(url = data_parse.img_list(imgdata)[0])
                        embed_lol.set_footer(text = f"此機器人已在 {len(self.bot.guilds)} 個伺服器中服務" + '\n' + '原始資料來自: https://lol.moa.tw/' + '\n' + find_time.text.replace('Last Modified date','最後更新日期'))
                        await ctx.respond(embed = embed_lol)
                        print(f'lol search at {nowtime()} response code : {response.status_code}')
            except:
                embed_lol = discord.Embed(title = '玩家查詢', description = '**查無此玩家**', colour = discord.Color.blue())
                await ctx.respond(embed = embed_lol)
                
                            
        
                    
def setup(bot):
    bot.add_cog(lol_search(bot))