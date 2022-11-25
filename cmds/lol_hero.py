from discord.ext import commands
import discord
import cloudscraper
import unicodedata
from bs4 import BeautifulSoup
from core.classes import data_parse
from core.classes import Cog_Extension
from core.translate import translate
from core.heros import heros
from discord.commands import Option
import time

def nowtime():
    sec = time.time()
    now = time.localtime(sec)
    str = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour+8}:{now.tm_min}:{now.tm_sec} UTC+8")
    return str

#LOL 英雄資料查詢
class lol_hero(Cog_Extension):
    @commands.slash_command(name = '查英雄', description = 'LOL英雄對抗查詢' )
    async def hero(self,ctx, 英雄: Option(str,'英雄名稱', required = True, default = ''), 
                             路線: Option(str,'英雄路線', required = False, default = '')):
        hero = 英雄
        lane = 路線
        lane = translate.lane(lane)
        list_hero = []
        if hero.encode('UTF-8').isalpha():
            sc = cloudscraper.create_scraper()
            headers = {"Accept-Language": "zh-TW"}
            if lane  == '':
                r = sc.get(f'https://www.op.gg/champions/{hero}', headers = headers)
                print(f'https://www.op.gg/champions/{hero}')
                soup = BeautifulSoup(r.text,"html.parser")
            else:
                r = sc.get(f'https://www.op.gg/champions/{hero}/{lane}/build?region=kr&tier=platinum_plus', headers = headers)
                print(f'https://www.op.gg/champions/{hero}/{lane}/build?region=kr&tier=platinum_plus')
                soup = BeautifulSoup(r.text,"html.parser")
            try:
                sel_name = soup.find_all('span', class_ = 'name')
                '''sel_tier = soup.find_all('div', class_ = 'css-brbf14 ew1oorz5')
                sel_rate = soup.find_all('div', class_ = 'css-oxevym ew1oorz4')'''
                sel_img = soup.find('div', class_ = 'img-box').find_all('img')
                sel_tier_img = soup.find('div', class_ = 'tier-icon').find_all('img')
                sel_count_img = soup.find('div', class_ = 'css-1o74if1 eoarhn86').find_all('img')
                sel_counter = soup.find('div', class_ = 'css-1o74if1 eoarhn86').find_all('div', class_ = 'win-rate')
                sel_lane = soup.find('div', class_ = 'info-box').select('h1')
                lanes = unicodedata.normalize("NFKD",sel_lane[0].text)
                lanes = lanes.split(' ')
                if sel_counter == []:
                    embed_hero = discord.Embed(title = f'{sel_name[0].text} 路線: {lanes[2]}', colour = discord.Colour.blue())
                    embed_hero.set_thumbnail(url = data_parse.img_list(sel_img)[0])
                    embed_hero.add_field(name = '此英雄沒有資料', value = '\u200B', inline = True)
                    await ctx.respond(embed = embed_hero)
                    print(f'lol hero search at {nowtime()} response code : {r.status_code}')
                else:
                    try:
                        tier = translate.tier(data_parse.img_list(sel_tier_img)[0])
                        list_hero = data_parse.img_list(sel_count_img)
                        embed_hero = discord.Embed(title = f'{sel_name[0].text} 路線: {lanes[2]} \nTier: {tier}', colour = discord.Colour.blue())
                        embed_hero.set_thumbnail(url = data_parse.img_list(sel_img)[1])
                        '''embed_hero.add_field(name = sel_tier[0].text.replace('階級', '勝率'), value = sel_rate[0].text, inline = True)
                        embed_hero.add_field(name = sel_tier[1].text, value = sel_rate[1].text, inline = True)
                        embed_hero.add_field(name = sel_tier[2].text, value = sel_rate[2].text, inline = True)'''
                        embed_hero.add_field(name = '好打的英雄', value = heros.hero_img(list_hero[5]) + '\n' + sel_counter[5].text, inline = True)
                        embed_hero.add_field(name = '\u200B', value = heros.hero_img(list_hero[6]) + '\n' + sel_counter[6].text, inline = True)
                        embed_hero.add_field(name = '\u200B', value = heros.hero_img(list_hero[7]) + '\n' + sel_counter[7].text, inline = True)
                        embed_hero.add_field(name = '難打的英雄', value = heros.hero_img(list_hero[0]) + '\n' + sel_counter[0].text, inline = True)
                        embed_hero.add_field(name = '\u200B', value = heros.hero_img(list_hero[1]) + '\n' + sel_counter[1].text, inline = True)
                        embed_hero.add_field(name = '\u200B', value = heros.hero_img(list_hero[2]) + '\n' + sel_counter[2].text, inline = True)
                        embed_hero.set_footer(text = f"此機器人已在 {len(self.bot.guilds)} 個伺服器中服務" + '\n' + '原始資料來自: https://www.op.gg/champions')
                        await ctx.respond(embed = embed_hero)
                        print(f'lol hero search at {nowtime()} response code : {r.status_code}')
                    except:
                        tier = translate.tier(data_parse.img_list(sel_tier_img)[0])
                        list_hero = data_parse.img_list(sel_count_img)
                        embed_hero = discord.Embed(title = f'{sel_name[0].text} 路線: {lanes[2]} \nTier: {tier}', colour = discord.Colour.blue())
                        embed_hero.set_thumbnail(url = data_parse.img_list(sel_img)[1])
                        '''embed_hero.add_field(name = sel_tier[0].text.replace('階級', '勝率'), value = sel_rate[0].text, inline = True)
                        embed_hero.add_field(name = sel_tier[1].text, value = sel_rate[1].text, inline = True)
                        embed_hero.add_field(name = sel_tier[2].text, value = sel_rate[2].text, inline = True)'''
                        embed_hero.add_field(name = '好打的英雄', value = '此英雄目前資料不足', inline = True)
                        embed_hero.add_field(name = '難打的英雄', value = '此英雄目前資料不足', inline = True)
                        embed_hero.set_footer(text = f"此機器人已在 {len(self.bot.guilds)} 個伺服器中服務" + '\n' + '原始資料來自: https://www.op.gg/champions')
                        await ctx.respond(embed = embed_hero)
                        print(f'lol hero search at {nowtime()} response code : {r.status_code}')
            except:
                hero = 英雄
                embed_hero = discord.Embed(title = '查英雄', description = f'查無此英雄 `{hero}`', colour = discord.Colour.blue())
                await ctx.respond(embed = embed_hero)
        else:
            hero = translate.hero(hero)
            sc = cloudscraper.create_scraper()
            headers = {"Accept-Language": "zh-TW"}
            r = sc.get(f'https://www.op.gg/champions/{hero}', headers = headers)
            soup = BeautifulSoup(r.text,"html.parser")
            try:
                sel_name = soup.find_all('span', class_ = 'name')
                '''sel_tier = soup.find_all('div', class_ = 'css-brbf14 ew1oorz5')
                sel_rate = soup.find_all('div', class_ = 'css-oxevym ew1oorz4')'''
                sel_img = soup.find('div', class_ = 'img-box').find_all('img')
                sel_tier_img = soup.find('div', class_ = 'tier-icon').find_all('img')
                sel_count_img = soup.find('div', class_ = 'css-1o74if1 eoarhn86').find_all('img')
                sel_counter = soup.find('div', class_ = 'css-1o74if1 eoarhn86').find_all('div', class_ = 'win-rate')
                sel_lane = soup.find('div', class_ = 'info-box').select('h1')
                lanes = unicodedata.normalize("NFKD",sel_lane[0].text)
                lanes = lanes.split(' ')
                if sel_counter == []:
                    embed_hero = discord.Embed(title = f'{sel_name[0].text} 路線: {lanes[2]}', colour = discord.Colour.blue())
                    embed_hero.set_thumbnail(url = data_parse.img_list(sel_img)[0])
                    embed_hero.add_field(name = '此英雄沒有資料', value = '\u200B', inline = True)
                    await ctx.respond(embed = embed_hero)
                    print(f'lol hero search at {nowtime()} response code : {r.status_code}')
                else:
                    try:
                        tier = translate.tier(data_parse.img_list(sel_tier_img)[0])
                        list_hero = data_parse.img_list(sel_count_img)
                        embed_hero = discord.Embed(title = f'{sel_name[0].text} 路線: {lanes[2]} \nTier: {tier}', colour = discord.Colour.blue())
                        embed_hero.set_thumbnail(url = data_parse.img_list(sel_img)[1])
                        '''embed_hero.add_field(name = sel_tier[0].text.replace('階級', '勝率'), value = sel_rate[0].text, inline = True)
                        embed_hero.add_field(name = sel_tier[1].text, value = sel_rate[1].text, inline = True)
                        embed_hero.add_field(name = sel_tier[2].text, value = sel_rate[2].text, inline = True)'''
                        embed_hero.add_field(name = '好打的英雄', value = heros.hero_img(list_hero[5]) + '\n' + sel_counter[5].text, inline = True)
                        embed_hero.add_field(name = '\u200B', value = heros.hero_img(list_hero[6]) + '\n' + sel_counter[6].text, inline = True)
                        embed_hero.add_field(name = '\u200B', value = heros.hero_img(list_hero[7]) + '\n' + sel_counter[7].text, inline = True)
                        embed_hero.add_field(name = '難打的英雄', value = heros.hero_img(list_hero[0]) + '\n' + sel_counter[0].text, inline = True)
                        embed_hero.add_field(name = '\u200B', value = heros.hero_img(list_hero[1]) + '\n' + sel_counter[1].text, inline = True)
                        embed_hero.add_field(name = '\u200B', value = heros.hero_img(list_hero[2]) + '\n' + sel_counter[2].text, inline = True)
                        embed_hero.set_footer(text = f"此機器人已在 {len(self.bot.guilds)} 個伺服器中服務" + '\n' + '原始資料來自: https://www.op.gg/champions')
                        await ctx.respond(embed = embed_hero)
                        print(f'lol hero search at {nowtime()} response code : {r.status_code}')
                    except:
                        tier = translate.tier(data_parse.img_list(sel_tier_img)[0])
                        list_hero = data_parse.img_list(sel_count_img)
                        embed_hero = discord.Embed(title = f'{sel_name[0].text} 路線: {lanes[2]} \nTier: {tier}', colour = discord.Colour.blue())
                        embed_hero.set_thumbnail(url = data_parse.img_list(sel_img)[1])
                        '''embed_hero.add_field(name = sel_tier[0].text.replace('階級', '勝率'), value = sel_rate[0].text, inline = True)
                        embed_hero.add_field(name = sel_tier[1].text, value = sel_rate[1].text, inline = True)
                        embed_hero.add_field(name = sel_tier[2].text, value = sel_rate[2].text, inline = True)'''
                        embed_hero.add_field(name = '好打的英雄', value = '此英雄目前資料不足', inline = True)
                        embed_hero.add_field(name = '難打的英雄', value = '此英雄目前資料不足', inline = True)
                        embed_hero.set_footer(text = f"此機器人已在 {len(self.bot.guilds)} 個伺服器中服務" + '\n' + '原始資料來自: https://www.op.gg/champions')
                        await ctx.respond(embed = embed_hero)
                        print(f'lol hero search at {nowtime()} response code : {r.status_code}')
            except:
                hero = 英雄
                embed_hero = discord.Embed(title = '查英雄', description = f'查無此英雄 `{hero}`', colour = discord.Colour.blue())
                await ctx.respond(embed = embed_hero)
        
        
def setup(bot):
    bot.add_cog(lol_hero(bot))