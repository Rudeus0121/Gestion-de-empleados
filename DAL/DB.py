import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="gestión de empleados")

# Get a cursor
cursor = cnx.cursor()

# Execute a query
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

#    Fetch one result
#    row = cursor.fetchone()
#    print("Current date is: {0}".format(row[0]))

#Close connection
cnx.close()