import sqlite3
con=sqlite3.connect("kütüphane1.db")
cursor=con.cursor()

def tablo_create():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Yazar TEXT, Yayınevi TEXT,Sayfa_sayısı INT)")
    con.commit()
tablo_create()
con.close()    # bu dosyanın olduğu klasöre kütühane1 adlı db uzantılı bir
#dosyo oluştu....

