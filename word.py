import sqlite3
import random
import os
import datetime


class Word(object):
    def __init__(self,limit=5,*data):
        self.limit = limit
        self.id         = data[0] if len(data)>0 else ""
        self.word       = data[1] if len(data)>1 else ""
        self.extra      = data[2] if len(data)>2 else ""
        self.point      = data[3] if len(data)>3 else ""
        self.last_time  = data[4] if len(data)>4 else ""
        if len(data)!=5:
            self.get()

    def get(self):
        path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
        con = sqlite3.connect(f"{path}/db.db")
        cur = con.cursor()
        sql = f"""
               select * from word where 
                (point<100 )or
                (point between 100 and (((point/100)*100)+100) and
                cast(julianday('now')-julianday(last_time) as INTEGER)>=6)
                limit {self.limit}
                """
        try:
            data = cur.execute(sql).fetchall()
            con.commit()
            index = random.randint(0,self.limit-1)
            data = data[index]
            if len(data)>0:
                self.id         = data[0]
                self.word       = data[1]
                self.extra      = data[2]
                self.point      = data[3]
                self.last_time  = data[4]


        except sqlite3.Error: pass
        finally:     
                cur.close()
                con.close()
    @staticmethod
    def get_info():
        ret = ('unknow',0)
        path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
        con = sqlite3.connect(f"{path}/db.db")
        cur = con.cursor()
        sql = f"""select u.user,sum(w.point)/50000+1 from word w,user u"""
        try:
            ret = cur.execute(sql).fetchone()
        except sqlite3.Error: pass
        finally:     
            cur.close()
            con.close()
            return ret
    def update(self):
            sql =  f"""update word set word='{self.word}',
                                    extra='{self.extra}',
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

class Word_trans(object):
    def __init__(self,*data):
        self.id         = data[0] if len(data)>0 else ""
        self.word_id    = data[1] if len(data)>1 else ""
        self.word       = data[1] if len(data)>1 else ""
        self.extra      = data[2] if len(data)>2 else ""
        self.lang_code  = data[3] if len(data)>3 else ""
        if len(data)!=5:
            self.get()

    def get(self):
        path = f"{os.sep}".join(os.path.realpath(__file__).split(os.sep)[:-1])
        con = sqlite3.connect(f"{path}/db.db")
        cur = con.cursor()
        sql = f"""
                select * from word_trans where 
                word_id={self.word_id}
            """
        try:
            data = cur.execute(sql).fetchall()
            con.commit()
            if len(data)>0:
                self.id         = data[0][0] 
                self.word_id    = data[0][1] 
                self.word       = data[0][2] 
                self.extra      = data[0][3] 
                self.lang_code  = data[0][4] 
        except sqlite3.Error: pass
        finally:     
                cur.close()
                con.close()
    
    def update(self):
            sql =  f"""update word set 
                                    word='{self.word}',
                                    word_id='{self.word_id}',
                                    extra='{self.extra}',
                                    lang_code='{self.lang_code}' 
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

