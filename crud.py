import sqlite3
# Connect to sqlite database
conn = sqlite3.connect('students.db')  #connecting
# cursor object
cursor = conn.cursor()
# drop query
cursor.execute("DROP TABLE IF EXISTS STUDENT")
# create query
query = """CREATE TABLE STUDENT(      
        ID INT PRIMARY KEY NOT NULL,
        NAME CHAR(20) NOT NULL, 
        ROLL CHAR(20), 
        ADDRESS CHAR(50), 
        CLASS CHAR(20) )"""
cursor.execute(query)

# Insert
conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
             "VALUES (1, 'John', '001', 'Vilnius', '10th')")
conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
             "VALUES (2, 'Naren', '002', 'Kaunas', '12th')")
conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
             "VALUES (3, 'Liwa', '003', 'Kaunas', '9th')")
# Update
conn.execute("UPDATE STUDENT set ROLL = 005 where ID = 1")
conn.commit()

# Delete
conn.execute("DELETE from STUDENT where ID = 2;")

# Read
read = conn.execute("SELECT * from STUDENT")
print(read.fetchall())

# commit and close
conn.commit()
conn.close()