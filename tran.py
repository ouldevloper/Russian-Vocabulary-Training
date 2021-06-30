# -*- utf-8 -*-
from os import error
from reverso_api.context import ReversoContextAPI, Translation
import sqlite3
import re

def get_all_Verbs():
    try:
        con = sqlite3.connect('verbs.db')
        cur = con.cursor()
        sql_ru = "select id,ru_verb from verbs"
        res = cur.execute(sql_ru).fetchall()
        con.commit()
        return res
    except sqlite3.Error:
        return None
        
    finally:
        cur.close()
        con.close()
    return None

def get_most_common(data:Translation):
    try:
        output = []
        for _data in data:
            output.append([_data.translation,_data.frequency])
        output = sorted(output,key=lambda x:x[1],reverse=True)
        items_lenght = len(output)
        sum_frequency = sum(list(map(lambda x:x[1],output)))
        if sum_frequency!=0 and items_lenght!=0:
            avg = (sum_frequency//items_lenght)
            return list(map(lambda x:x[0],filter(lambda x:x[1]>=avg,output)))
        else:
            return list(map(lambda x:x[0],output))
    except Exception as err:
        print ("Function get_most_common : line 37 : ",err)
    return []

def get_translaion(source:str="help",translate:str="",_from:str="ru",to:str="ar"):
    try:
        api = ReversoContextAPI(source,translate,_from,to)   
        return api.get_translations()
    except Exception as err:
        print ("Function get_translaion : line 45 : ",err)
    return []

def add_to_db(id=0,ru_id="",verb="",table_name="ar_trans"):
    try:
        con = sqlite3.connect('verbs.db')
        cur = con.cursor()
        verbs = get_all_Verbs()
        index = 1
        for ind,verb in enumerate(verbs):
            _id = verb[0]
            _verb = verb[1]
            trans = get_translaion(_verb,"","ru","ar")
            common = get_most_common(trans)
            if len(common)>0:
                try:
                    print(f"[+] {index} Done.  ",_verb," <==> ",common[0])
                    sql = f"insert into ar_trans values ('{ind+1}','{_id}',\"{common[0]}\")"
                    res = cur.execute(sql)
                    con.commit()
                    index+=1
                except sqlite3.Error as er:
                    print(er)
                
            #for data in common:
            #    sql = f"insert into en_trans values ('{index}','{_id}',\"{data}\")"
            #    res = cur.execute(sql)
            #    con.commit()
            #    print(f"[+] {index} Done.")
            #    index+=1
    except sqlite3.Error as er:
        print("line 61")
        print(er)
        print(verb,_id,_verb)
    else:
        return True
    finally:
        cur.close()
        con.close()
    return None   

def from_same_table():
    con = sqlite3.connect('verbs.db')
    cur = con.cursor()
    data = cur.execute("select  id,en_verb_complete from verbs").fetchall()
    cur.execute("delete from en_trans")
    con.commit()
    index=1
    for d in data:
        en_verbs = d[1].replace("imperfective","").replace("imperf","").replace("perfective","")
        en_verbs = re.sub(r'\(.+\)',"",en_verbs)
        en_verbs = en_verbs.strip().split(',')
        for ver in en_verbs:
            sql = f"insert into en_trans values ('{index}','{d[0]}',\"{ver}\")"
            res = cur.execute(sql)
            con.commit()
            index+=1
            print(f'{index} Done.')
            
def marge_dbs():
    db_1 = sqlite3.connect("db.db")
    cur_1 = db_1.cursor()
    db_2 = sqlite3.connect("verbs.db")
    cur_2 =db_2.cursor()
    try:

        for row in cur_1.execute("select * from words").fetchall():
            cur_2.execute(f"update word set extra='{row[3]}' where id='{row[0]}'")
            #cur_2.execute(f"insert into word_trans values('{row[0]}','{row[0]}','en','{row[2]}','{row[4]}')")
            db_2.commit()
            print(f"{row[0]} Done.")
    except sqlite3.Error as er:
        print(er)

def edit_ru_firld():

    db_2 = sqlite3.connect("verbs.db")
    cur_2 =db_2.cursor()
    try:

        for row in cur_2.execute("select * from word_trans").fetchall():
            sql = f"""
                update word_trans set word='{row[3]}',
                                    extra = '{row[4]}',lang_code='{row[2]}'
                                    where id = '{row[0]}'
            """
            cur_2.execute(sql)
            db_2.commit()
            print(f"{row[0]} Done.")
    except sqlite3.Error as er:
        print(er)
