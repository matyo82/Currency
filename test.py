from mysql.connector import connect

mydb = connect(
    host="localhost",
    user="root",
    password="123",
    database="arz"
)
mycursor = mydb.cursor()

sql = "UPDATE `price` SET `price` = %s WHERE price.name = %s; "
val = ('500000', 'دلار')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, " add in table")

# for update "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"


# create a data base
# mycursor.execute("CREATE DATABASE mydatabase")

# show databases //// baraye namayesh bayad for zad!
# mycursor.execute("SHOW DATABASES")

# create table in databases
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# show tables
# mycursor.execute("SHOW TABLES")

# alter musql:
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# for insert data in table:
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()
# show how mani insert:
# print(mycursor.rowcount, "record inserted.")

# if you insert two and ... use:
#  mycursor.executemany(sql, val)

# select and show data
# mycursor.execute("SELECT * FROM customers")

# for update "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"