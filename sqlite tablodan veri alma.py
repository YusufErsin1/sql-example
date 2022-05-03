import sqlite3
con=sqlite3.connect("kütüphane1.db")
cursor=con.cursor()
def data_take():
    cursor.execute("select * from kitaplık")
    list1=cursor.fetchall()
    for i in list1:
        print(i)
def data_take2():
    cursor.execute("select İsim,yazar from kitaplık")
    list2=cursor.fetchall()
    print(list2)
def data_take3(yayinevi):
    cursor.execute("select * from kitaplık where yayınevi=?",(yayinevi,))
    list3=cursor.fetchall()
    for i in list3:
        print(i[1])
#data_take()
#data_take2()
data_take3("Pegasus")
con.close()


