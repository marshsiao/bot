import discord
import psycopg2
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
class data_parse:
    def split_list(lst,n):
        for i in range(0, len(lst), n):
            yield lst[i : i+n]
    
    def split_list_ids(lst,n):
        if len(lst) <= n:
            return lst
        elif len(lst) > n:
            for i in range(0, len(lst), n):
                yield lst[i : i+n]
            
    def cutlist(lst):
        list_return = []
        for i in range((len(lst)-10),len(lst)):
            string = ''
            string = lst[i].text
            list_return.append(string)
        return list_return
    
    def cutlist_2(lst):
        list_return = []
        for i in range((len(lst)-10),len(lst)):
            string = ''
            string = lst[i]
            list_return.append(string)
        return list_return

    def create_string_list(lst):
        string = ''
        for item in lst:
            string += item.text + '\n'
        return string

    def create_string_2(lst):
        string = ''
        for item in lst:
            string += item.text + ' '
        return string
    
    def create_string(lst):
        string = ''
        for item in lst:
            string += item + '\n'
        return string

    def list_zip(lst_1,lst_2):
        string = ''
        for i in range(0,len(lst_1)):
            string += str(lst_1[i] + ' ' + lst_2[i].text) + '\n'
        return string
    
    def list_zip_2(lst_1,lst_2):
        string = ''
        for i in range(0,len(lst_1)):
            string += str(lst_1[i] + ' ' + lst_2[i]) + '\n'
        return string


    def img_list(lst_1):
        lst_2 = []
        for i in range(len(lst_1)):
            lst_2.insert(i,lst_1[i].attrs["src"])
        return lst_2

    def create_name(tupl):
        s = ''
        if len(tupl) == 1:
            s = tupl[0]
            return s
        elif len(tupl) >= 2:
            s = tupl[0]
            for i in range(1,len(tupl)):
                s += '%20'+tupl[i]
            return s 
    
    def create_quot(tupl):
        s = ''
        if len(tupl) == 1:
            s = tupl[0]
            return s
        elif len(tupl) >= 2:
            s = tupl[0]
            for i in range(1,len(tupl)):
                s += ' '+tupl[i]
            return s
    
    def create_viewquot(lst):
        s = ''
        if len(lst) == 1:
            s = lst[0]
            return s
        else:
            s = lst[0]
            for i in range(1,len(lst)):
                s += '\n' + '-----------------' + '\n' + lst[i]
            return s
    
    def translate(lst1):
        list_return = []
        for i in range(0,len(lst1)):
            s = ''
            if lst1[i].text == 'Unranked':
                s = lst1[i].text.replace('Unranked','未參與積分')
            elif lst1[i].text == 'Bronze':
                s = lst1[i].text.replace('Bronze','青銅')
            elif lst1[i].text == 'Silver':
                s = lst1[i].text.replace('Silver','白銀')
            elif lst1[i].text == 'Gold':
                s = lst1[i].text.replace('Gold','黃金')
            elif lst1[i].text == 'Platinum':
                s = lst1[i].text.replace('Platinum','白金')
            elif lst1[i].text == 'Diamond':
                s = lst1[i].text.replace('Diamond','鑽石')
            elif lst1[i].text == 'Master':
                s = lst1[i].text.replace('Master','大師')
            elif lst1[i].text == 'Grandmaster':
                s = lst1[i].text.replace('Grandmaster','宗師')
            elif lst1[i].text == 'Challenger':
                s = lst1[i].text.replace('Challenger','菁英')
            list_return.append(s)
        return list_return
    
'''class database():
    def create_table(guild_id):
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        table_name = f"datas_{guild_id}"
        createtable = str("CREATE TABLE if not exists " + table_name + " (id serial PRIMARY KEY, name VARCHAR(50), value VARCHAR(50));")
        cur.execute(createtable)
        conn.commit()
        cur.close()
        conn.close()
    
    def create_initdata(guild_id):
        table_name = f"datas_{guild_id}"
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        createtable = str("CREATE TABLE if not exists " + table_name + " (id serial PRIMARY KEY, name VARCHAR(50), value VARCHAR(50));")
        cur.execute(createtable)
        cur.execute("INSERT INTO " + table_name + " (name, value) VALUES (%s, %s);", ("acct_id", "false"))
        cur.execute("INSERT INTO " + table_name + " (name, value) VALUES (%s, %s);", ("lol_search_all_id", "false"))
        cur.execute("INSERT INTO " + table_name + " (name, value) VALUES (%s, %s);", ("server_management", "false"))
        conn.commit()
        cur.close()
        conn.close()
        
    def create_initsaysdata(guild_id):
        table_name = f"saysdatas_{guild_id}"
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        createtable = str("CREATE TABLE if not exists " + table_name + " (id serial PRIMARY KEY, name VARCHAR(100));")
        cur.execute(createtable)
        conn.commit()
        cur.close()
        conn.close()

    def insert_data(guild_id,val_1,val_2):
        table_name = f"datas_{guild_id}"
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO " + table_name + " (name, value) VALUES (%s, %s);", (val_1, val_2))
        conn.commit()
        cur.close()
        conn.close()
    
    def insert_saysdata(guild_id,val_1):
        table_name = f"saysdatas_{guild_id}"
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO " + table_name + " (name) VALUES (%s);", (val_1,))
        conn.commit()
        cur.close()
        conn.close()
    
    def del_data(guild_id,val_1):
        table_name = f"datas_{guild_id}"
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        cur.execute("DELETE FROM " + table_name + " WHERE name = %s;", (val_1,))
        conn.commit()
        cur.close()
        conn.close()
        
    def del_saysdata(guild_id,val_1):
        table_name = f"saysdatas_{guild_id}"
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        cur.execute("DELETE FROM " + table_name + " WHERE name = %s;", (val_1,))
        conn.commit()
        cur.close()
        conn.close()
    
    def select_data(guild_id,name):
        try:
            table_name = f"datas_{guild_id}"
            conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
            cur = conn.cursor()
            cur.execute("SELECT value FROM " + table_name + " WHERE name = %s;", (name,))
            rows = cur.fetchall()
            value = rows[0]
            conn.commit()
            cur.close()
            conn.close()
            return value[0]
        except:
            table_name = f"datas_{guild_id}"
            conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
            cur = conn.cursor()
            createtable = str("CREATE TABLE if not exists " + table_name + " (id serial PRIMARY KEY, name VARCHAR(50), value VARCHAR(50));")
            cur.execute(createtable)
            cur.execute("INSERT INTO " + table_name + " (name, value) VALUES (%s, %s);", (name, "false"))
            cur.execute("SELECT value FROM " + table_name + " WHERE name = %s;", (name,))
            rows = cur.fetchall()
            value = rows[0]
            conn.commit()
            cur.close()
            conn.close()
            return value[0]
    
    def update_data(guild_id,val_1,val_2):
        table_name = f"datas_{guild_id}"
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        cur.execute("UPDATE " + table_name + " SET value = %s" + " WHERE name = %s;", (val_2,val_1))
        conn.commit()
        cur.close()
        conn.close()
    
    def view_data(guild_id):
        table_name = f"datas_{guild_id}"
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
                            user="akujhujesaztrp",
                            password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
                            host="ec2-54-208-104-27.compute-1.amazonaws.com",
                            port="5432")
        cur = conn.cursor()
        cur.execute("SELECT value FROM " + table_name + " ORDER BY id ASC;")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        list_return = []
        for i in range(0,len(rows)):
            tuple_rows = rows[i]
            list_return.append(tuple_rows[0])
        return list_return
        
    def view_saysdata(guild_id):
        table_name = f"saysdatas_{guild_id}"
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
                            user="akujhujesaztrp",
                            password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
                            host="ec2-54-208-104-27.compute-1.amazonaws.com",
                            port="5432")
        cur = conn.cursor()
        createtable = str("CREATE TABLE if not exists " + table_name + " (id serial PRIMARY KEY, name VARCHAR(100));")
        cur.execute(createtable)
        cur.execute("SELECT name FROM " + table_name + " ORDER BY id ASC;")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        list_return = []
        for i in range(0,len(rows)):
            tuple_rows = rows[i]
            list_return.append(tuple_rows[0])
        return list_return
    
    def drop_table(guild_id):
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        table_name = f"datas_{guild_id}"
        createtable = str("DROP TABLE if exists " + table_name + ";")
        cur.execute(createtable)
        conn.commit()
        cur.close()
        conn.close()
        
    def drop_saystable(guild_id):
        conn = psycopg2.connect(database="dcnd6gtvg7l619",
						user="akujhujesaztrp",
						password="6826518f230a809794faf795ed0c221fe8cf1ba758ea24b1228cb76a9456daef",
						host="ec2-54-208-104-27.compute-1.amazonaws.com",
						port="5432")
        cur = conn.cursor()
        table_name = f"saysdatas_{guild_id}"
        createtable = str("DROP TABLE if exists " + table_name + ";")
        cur.execute(createtable)
        conn.commit()
        cur.close()
        conn.close()'''
    
            