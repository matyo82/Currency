from mysql.connector import connect
import dataItem
mydb = connect(
    host=dataItem.host,
    user=dataItem.user,
    password=dataItem.password,
    database=dataItem.database
)
mycursor = mydb.cursor()

def addTodatabase(name, price):
    sql = f"INSERT INTO {dataItem.table} (name, price) VALUES (%s, %s)"
    val = (name, price)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount," add in table")

def updatePrice(price, name):
    sql = "UPDATE {dataItem.table} SET `price` = %s WHERE price.name = %s; "
    val = (price, name)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, " update price for: ", name)

def showPrice():
    mycursor.execute("SELECT * FROM {dataItem.table}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(f'name: {x[1]} - price: {x[2]}')