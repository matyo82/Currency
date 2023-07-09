from mysql.connector import connect

mydb = connect(
    host="localhost",
    user="root",
    password="123",
    database="arz"
)
mycursor = mydb.cursor()

def addTodatabase(name, price):
    sql = "INSERT INTO price (name, price) VALUES (%s, %s)"
    val = (name, price)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount," add in table")

def updatePrice(price, name)
    sql = "UPDATE `price` SET `price` = %s WHERE price.name = %s; "
    val = (price, name)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, " update price for: ",name)
