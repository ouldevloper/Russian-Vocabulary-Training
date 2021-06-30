import sqlite3
import random
import datetime
import sys
import os


class verb:
        def __init__(self,limit,*data):
                self.limit = limit
                self.id               = data[0] if len(data)>=1 else ""
                self.ru_verb          = data[1] if len(data)>=2 else ""
                self.ru_complete_verb = data[2] if len(data)>=3 else ""
                self.en_complete_verb = data[3] if len(data)>=4 else ""
                self.point            = data[4] if len(data)>=5 else ""
                self.last_date        = data[5] if len(data)>=6 else ""
                if not data:
                        self.get()

        def get(self):
                path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
                con = sqlite3.connect(f"{path}/db.db")
                cur = con.cursor()
                sql = f"""
                        select * from verbs where 
                        (point<100 and  cast(julianday('now')-julianday(last_time) as INTEGER)<6)or
                        ((((point/100)*100)+100)>point and point>100 and
                        cast(julianday('now')-julianday(last_time) as INTEGER)>=6)
                        limit {self.limit}
                      """
                try:
                        data = cur.execute(sql).fetchall()
                        con.commit()
                        index = random.randint(0,self.limit-1)
                        data = data[index]
                        self.id               = data[0]
                        self.ru_verb          = data[1]
                        self.ru_complete_verb = data[2]
                        self.en_complete_verb = data[3]
                        self.point            = data[4]
                        self.last_date        = data[5]

                except sqlite3.Error: pass
                finally:     
                        cur.close()
                        con.close()

                
        @staticmethod
        def get_level():
                ret = ('unknow',0)
                path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
                con = sqlite3.connect(f"{path}/db.db")
                cur = con.cursor()
                sql = f"""select u.user,sum(v.point)/500+1 from verbs v,user u"""
                try:
                        ret = cur.execute(sql).fetchone()
                except sqlite3.Error: pass
                finally:     
                        cur.close()
                        con.close()

                return ret
        def update(self):
                sql =  f"""update verbs set ru_verb='{self.ru_verb}',
                                       ru_verb_complete='{self.ru_complete_verb}',
                                       en_verb_complete='{self.en_complete_verb}',
                                       point='{self.point}',
                                       last_time='{str(datetime.datetime.now())[:10]}' 
                                       where id='{self.id}'
                        """
                path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
                con = sqlite3.connect(f"{path}/db.db")
                cur = con.cursor()
                try:
                        data = cur.execute(sql)
                        con.commit()
                finally:        
                        cur.close()
                        con.close()
                        
class Settings:
        def __init__(self,*data):
                self.id = 1
                self.native_lang = 'ar'
                self.foreing_lang = 'en'
                if len(data)!=3:
                        self.get()
                else:
                        self.id           = data[0]
                        self.native_lang  = data[1]
                        self.foreing_lang = data[2]


        def get(self):
                ret = (self.id,self.native_lang,self.foreing_lang)
                sql = "select * from settings"
                path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
                con = sqlite3.connect(f"{path}/db.db")
                cur  = con.cursor()
                try:
                        res = cur.execute(sql)
                        con.commit()
                        ret = res.fetchone()
                        self.id = ret[0]
                        self.native_lang = ret[1]
                        self.foreing_lang = ret[2]
                except:
                        pass
                return ret

        def update(self):
                ret = False
                sql = f"UPDATE settings SET native_lang='{self.native_lang}',foreing_lang='{self.foreing_lang}' where id={self.id}"
                path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
                con = sqlite3.connect(f"{path}/db.db")
                cur  = con.cursor()
                try:
                        cur.execute(sql)
                        con.commit()
                        ret = True
                except:
                        ret = False
                return ret
        
class lang(object):
        def __init__(self,lang_code,ru_id=1):
                self.lang_code = lang_code
                self.ru_verb_id = ru_id
                
        def get(self):
                ret = ()
                sql = f"""select * from {self.lang_code}_trans where ru_verb_id={self.ru_verb_id}"""
                path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
                con = sqlite3.connect(f"{path}/db.db")
                cur  = con.cursor()
                try:
                        res = cur.execute(sql)
                        con.commit()
                        ret = res.fetchall()
                except:
                        pass

                return ret

class User(object):
        def __init__(self,*data):
                self.user = ""
                self.word_count = ""
                if len(data)!=2:
                        self.get()
                else:
                        self.user = data[0]
                        self.word_count = data[1]

        def get(self):
                ret = (self.user,self.word_count)
                sql = "select * from user"
                path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
                con = sqlite3.connect(f"{path}/db.db")
                cur  = con.cursor()
                try:
                        res = cur.execute(sql)
                        con.commit()
                        ret = res.fetchone()
                        self.user = ret[1]
                        self.word_count = ret[0]
                except:
                        pass
                return ret

        def update(self):
                ret = False
                sql = f"UPDATE user SET user='{self.user}',word_count='{self.word_count}'"
                path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
                con = sqlite3.connect(f"{path}/db.db")
                cur  = con.cursor()
                try:
                        cur.execute(sql)
                        con.commit()
                        ret = True
                except:
                        ret = False
                return ret


#class CRUD:
#        con=sqlite3.connect("db.db")
#        cur = con.cursor()
#        
#        def __init__(self):
#                pass
#        @staticmethod
#        def add(table_name,col_val:dict={}):
#                ret = False
#                con=sqlite3.connect("db.db")
#                cur = con.cursor()
#                cols = ",".join([name for name in col_val.keys()])
#                vals = "',".join([name for name in col_val.values()])
#                sql = f"INSERT  INTO {table_name} ({cols}) VALUES ('{vals}')"
#                []
#                try:
#                        cur.execute(sql)
#                        con.commit()
#                        ret = True
#                except sqlite3.Error:
#                        pass
#                finally:
#                        cur.close()
#                        con.close()
#                return ret
#
#        @staticmethod
#        def delete(table_name,conditions:str):
#                ret = False
#                con=sqlite3.connect("db.db")
#                cur = con.cursor()
#                sql = f"DELETE FROM  {table_name} WHERE  {conditions}"
#                try:
#                        cur.execute(sql)
#                        con.commit()
#                        ret = True
#                except sqlite3.Error:
#                        pass
#                finally:
#                        cur.close()
#                        con.close()
#                return ret
#        @staticmethod
#        def update():
#                pass
#        @staticmethod
#        def get():
#                pass
