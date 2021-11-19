import sqlite3


def selectOperasyonlari():
    connection = sqlite3.connect("chinook.db")
# # cursor = connection.execute("""select city,count(*)
# #                             from Customers group by city having count(*)>1 order by count(*) desc""")                   #having --> şehre göre grupla ve sayısı 1 den fazla olanları bana ver
# #
# #
# # for row in cursor:
# #     print("City = "+row[0])
# #     print("Count = "+str(row[1]))
# #     print("**********************************************")
#
#
# cursor = connection.execute("""select FirstName,LastName
#                            from customers
#                            where FirstName like '%aa%'  """)
#
# for row in cursor:
#     print("First Name = "+row[0])
#     print("Last Name = "+row[1])
#     # print("City = "+row[2])
#     print("**********************************************")
#
# connection.close()

    cursor = connection.execute("""select FirstName,LastName
                                from customers
                                where FirstName like '%ja' """)

    for row in cursor:
        print("First Name : "+row[0])
        print("Last Name : "+row[1])
        print("********************************************")

    connection.close()


selectOperasyonlari()

def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers
                        (FirstName,LastName,City,Email)
                        values('Recep','Mert','Istanbul','recep@mert.com')""")

    connection.commit()
    connection.close()

# insertCustomer()


def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set City = 'Ankara' 
                        where city='Istanbul' or city='Istanbul'""")

    connection.commit()
    connection.close()

# updateCustomer()


def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from customers 
                        where City='Ankara' or City='İstanbul'      """)

    connection.commit()
    connection.close()

# deleteCustomer()




def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")

    cursor = connection.execute("""select albums.Title, artists.Name 
                            from artists inner join albums
                            on artists.ArtistId = albums.ArtistId """)

    for row in cursor:
        print("Title : "+row[0]+" Name : "+row[1])

    connection.close()

# joinOperasyonlari()

