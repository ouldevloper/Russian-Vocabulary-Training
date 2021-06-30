import sqlite3

def add(id,ru_verb,ru_verb_complete,en_verb_complete):
    con = sqlite3.connect("verbs.db")
    cur = con.cursor()
    sql = f"insert into verbs values({id},'{ru_verb}','{ru_verb_complete}','{en_verb_complete}',0,'2021-06-22')"
    try:
        cur.execute(sql)
        con.commit()
        ##print(f"\r\r {id} Done.!")
    except:
        print("[-] Error in ",end='')
        print(id,"\t",ru_verb,"\t",ru_verb_complete,"\t",en_verb_complete)
id = 1
def parse(data):
    return data.strip("\n").strip().split(";")
for i in open("500russianverbs.txt","r"):
    data = parse(i)
    add(id,data[0],data[2],data[1])
    id+=1