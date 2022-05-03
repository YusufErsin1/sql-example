import sqlite3
con=sqlite3.connect("kütüphane1.db")
cursor=con.cursor()

def tablo_create():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Yazar TEXT, Yayınevi TEXT,Sayfa_sayısı INT)")
    con.commit()

def data_add():
    cursor.execute("Insert into kitaplık Values('İstanbul hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
data_add()
con.close() 
