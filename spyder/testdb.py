import sqlite3

conn = sqlite3.connect('testdb.db')
c = conn.cursor()
sql = '''
   create table company
       (ID int primary key not null,
       Name text not null,
       Age int not null,
       Adress char(50),
       Salary real)
'''
c.execute(sql)
conn.commit()
conn.close()

conn = sqlite3.connect('testdb.db')
c = conn.cursor()
sql = '''
    insert into company (ID, Name, Age, Adress, Salary)
        values(1, 'new', 43, 'zhengzhou', 10000)
'''
c.execute(sql)
conn.close()