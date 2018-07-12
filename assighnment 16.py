import sqlite3
conn=sqlite3.connect('text.db')

#Q1
conn.execute("CREATE TABLE BOOK1(BOOKID INT PRIMARY KEY NOT NULL,TITLEID INT NOT NULL,LOCATON CHAR[50],GENRE TEXT NOT NULL);")
conn.execute("CREATE TABLE TITLES1(TITLEID INT PRIMARY KEY NOT NULL,TITLE TEXT NOT NULL,ISBN INT NOT NULL,PUBLISHERID INT NOT NULL,PUBLICATIONYEAR INT NOT NULL);")
conn.execute("CREATE TABLE PUBLISHERS(PUBLISHERID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,STREETADDRESS TEXT NOT NULL,SUITENUMBER INT NOT NULL,ZIPCODEID INT NOT NULL);")
conn.execute("CREATE TABLE ZIPCODES(ZIPCODEID INT PRIMARY KEY NOT NULL,CITY TEXT NOT NULL,STATE TEXT NOT NULL,ZIPCODE INT NOT NULL);")
conn.execute("CREATE TABLE AUTHORSTITLES(AUTHORTITLEID INT PRIMARY KEY NOT NULL,AUTHORID INT NOT NULL,TITLEID INT NOT NULL);")
conn.execute("CREATE TABLE AUTHORS(AUTHORID INT PRIMARY KEY NOT NULL,FIRSTNAME TEXT NOT NULL,MIDDLENAME TEXT NOT NULL,LASTNAME TEXT NOT NULL);")
#Q2
conn.execute("INSERT INTO BOOK1(BOOKID,TITLEID,LOCATON,GENRE)VALUES(69,47,'KRGYSTAN','HISTORY')")
conn.execute("INSERT INTO TITLES1(TITLEID,TITLE,ISBN,PUBLISHERID,PUBLICATIONYEAR)VALUES(144,'HASTA LA VISTA',16,190,1998)")
conn.execute("INSERT INTO PUBLISHERS(PUBLISHERID,NAME,STREETADDRESS,SUITENUMBER,ZIPCODEID)VALUES(23,'ALBERTO DEL RIO','BAKING STREET',43,123)")
conn.execute("INSERT INTO ZIPCODES(ZIPCODEID,CITY,STATE,ZIPCODE)VALUES(214,'PUDUCHERRY','KERALA',13500)")
conn.execute("INSERT INTO AUTHORSTITLES(AUTHORTITLEID,AUTHORID,TITLEID)VALUES(211,209,231)")
conn.execute("INSERT INTO AUTHORS(AUTHORID,FIRSTNAME,MIDDLENAME,LASTNAME)VALUES(230,'MARVIN','WAIT FOR IT','ERIKSEN')")
conn.commit()
print("Sucesss")
#Q3

cursor=conn.execute("SELECT BOOKID,TITLEID,LOCATON,GENRE from BOOK1")
for row in cursor:
    print("BOOKID=",row[0])
    print("TITLEIDnew=",row[1])
    print("LOCATON=",row[2])
    print("GENRE=",row[3],"\n")


cursor=conn.execute("SELECT TITLEID,TITLE,ISBN,PUBLISHERID,PUBLICATIONYEAR from TITLES1")
for row in cursor:
    print("TITLEID=",row[0])
    print("TITLE=",row[1])
    print("ISBN=",row[2])
    print("PUBLISHERID=",row[3])
    print("PUBLICATIONYEAR=",row[4],"\n")

cursor=conn.execute(" SELECT PUBLISHERID,NAME,STREETADDRESS,SUITENUMBER,ZIPCODEID from PUBLISHERS")
for row in cursor:
    print("PUBLISHERID=",row[0])
    print("NAME=",row[1])
    print("STREETADDRESS=",row[2])
    print("SUITENUMBER=",row[3])
    print("ZIPCODEID=",row[4],"\n")

cursor=conn.execute("SELECT ZIPCODEID,CITY,STATE,ZIPCODE from ZIPCODES")
for row in cursor:
    print("ZIPCODEID=",row[0])
    print("CITY=",row[1])
    print("STATE=",row[2])
    print("ZIPCODE=",row[3],"\n")

cursor=conn.execute("SELECT AUTHORTITLEID,AUTHORID,TITLEID from AUTHORSTITLES")
for row in cursor:
    print("AUTHORTITLEID=",row[0])
    print("AUTHORID=",row[1])
    print("TITLEID=",row[2])

cursor=conn.execute("SELECT AUTHORID,FIRSTNAME,MIDDLENAME,LASTNAME from AUTHORS")
for row in cursor:
    print("AUTHORID=",row[0])
    print("FIRSTNAME=",row[1])
    print("MIDDLENAME=",row[2])
    print("LASTNAME",row[3],"\n")
conn.execute("UPDATE BOOK1 set TITLEID=56 where BOOKID=69")
conn.commit()
cursor=conn.execute("SELECT BOOKID,TITLEID,LOCATON,GENRE from BOOK1")
for row in cursor:
    print("BOOKID=",row[0])
    print("TITLEIDnew=",row[1])
    print("LOCATON=",row[2])
    print("GENRE=",row[3],"\n")

cursor=conn.execute("SELECT TITLEID,TITLE,ISBN,PUBLISHERID,PUBLICATIONYEAR from TITLES1")
for row in cursor:
    print("TITLEID=",row[0])
    print("TITLE=",row[1])
    print("ISBN=",row[2])
    print("PUBLISHERID=",row[3])
    print("PUBLICATIONYEAR=",row[4],"\n")

cursor=conn.execute(" SELECT PUBLISHERID,NAME,STREETADDRESS,SUITENUMBER,ZIPCODEID from PUBLISHERS")
for row in cursor:
    print("PUBLISHERID=",row[0])
    print("NAME=",row[1])
    print("STREETADDRESS=",row[2])
    print("SUITENUMBER=",row[3])
    print("ZIPCODEID=",row[4],"\n")

cursor=conn.execute("SELECT ZIPCODEID,CITY,STATE,ZIPCODE from ZIPCODES")
for row in cursor:
    print("ZIPCODEID=",row[0])
    print("CITY=",row[1])
    print("STATE=",row[2])
    print("ZIPCODE=",row[3],"\n")

cursor=conn.execute("SELECT AUTHORTITLEID,AUTHORID,TITLEID from AUTHORSTITLES")
for row in cursor:
    print("AUTHORTITLEID=",row[0])
    print("AUTHORID=",row[1])
    print("TITLEID=",row[2])

cursor=conn.execute("SELECT AUTHORID,FIRSTNAME,MIDDLENAME,LASTNAME from AUTHORS")
for row in cursor:
    print("AUTHORID=",row[0])
    print("FIRSTNAME=",row[1])
    print("MIDDLENAME=",row[2])
    print("LASTNAME",row[3],"\n")

