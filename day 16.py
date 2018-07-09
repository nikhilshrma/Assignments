#
#import sqlite3
#conn = sqlite3.connect('test.db')
#print("opened database successfully")
#conn.execute('''CREATE TABLE COMPANY
  #      (ID INT PRIMARY KEY NOT NULL,
   #     NAME TEXT NOT NULL,
    #    AGE INT NOT NULL,
     #   ADDRESS CHAR(50),
      #  SALARY REAL)''')
#print("Table created successfully")
#conn.close()
#
import sqlite3
conn = sqlite3.connect('test.db')
print("opened database successfully")
#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
 #   VALUES (1,'PAUL',32,'CALIFORNIA',20000)")
#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #VALUES (2,'ALLEN',25,'TEXAS',15000)")
#conn.commit()
#print("record created successfully")
#conn.close()
#
conn.execute("UPDATE COMPANY set SALARY = 250000 where ID=1")
conn.commit()
print(" Total number of rows updated :", conn.total_changes)
cursor = conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY FROM COMPANY")
for row in cursor:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("AGE=",row[2])
    print("ADDRESS=",row[3])
    print("salary=",row[4])
print("operation done zuccessfully")
conn.close()
#to delete the id we use delete

#

