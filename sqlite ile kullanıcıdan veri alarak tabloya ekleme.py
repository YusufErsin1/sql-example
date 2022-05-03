import sqlite3
con=sqlite3.connect("kütüphane1.db")
cursor=con.cursor()

def veri_add2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("insert into kitaplık values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
isim=input("Kitabın adı: ")
yazar=input("Yazarın adı: ")
yayinevi=input("yayınevi: ")
sayfa_sayisi=int(input("sayfa sayısı: "))
veri_add2(isim, yazar, yayinevi, sayfa_sayisi)
con.close()
