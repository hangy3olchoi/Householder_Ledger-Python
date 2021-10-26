'''
Created on 2021. 7. 22.

SQLite의 CRUD (C - Create(or Insert), R - Select, U - Update, D - Delete)
각 기능을 함수로 만들 수 있다.

@author: pc356
'''
import sqlite3

def createTable():
    # connection 객체 생성
    conn = sqlite3.connect('household_Leger.db') # isolation_level = None 생략
    
    # cursor 생성
    c = conn.cursor()
    c.execute('''
        create table if not exists ledger
        (serialNo integer primary key Autoincrement,
         date text,
         section text,
         title text,
         revenue text,
         expense text,
         remark text)
    ''')
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

# insert할 매개 변수    
def insertData(date, section, title, revenue, expense, remark):
    conn = sqlite3.connect('household_Leger.db')
    
    c = conn.cursor()
    c.execute('''
        insert into ledger(date, section, title, revenue, expense, remark)
        values(?, ?, ?, ?, ?, ?)
    ''',(date, section, title, revenue, expense, remark))# 매개 변수를 질의문에 넣는 방법
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

def insertManyData(tupleData):
    conn = sqlite3.connect('household_Leger.db')
    
    c = conn.cursor()
    c.executemany('''
        insert into ledger(date, section, title, revenue, expense, remark)
        values(?, ?, ?, ?, ?, ?)
    ''',tupleData)# 매개 변수를 질의문에 넣는 방법
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

def selectAll():
    conn = sqlite3.connect('household_Leger.db')

    c = conn.cursor()
    c.execute('select * from ledger')
    
    rows = c.fetchall()
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    return rows

    pass

def select(key):
    conn = sqlite3.connect('household_Leger.db')

    c = conn.cursor()
    c.execute('select * from ledger')
    
    rows = c.fetchall()
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    return rows

    pass

# vo는 dict로 만들어서 보냄
def update(vo): # vo는 tuple 형식임
    conn = sqlite3.connect('household_Leger.db')
    
    c = conn.cursor()
    c.execute('''
        update ledger set date = ?, section = ?, title = ?, revenue = ?, expense = ?, remark = ? where serialNo = ?
    ''',vo) # vo - tuple 형식(dict일 경우 복잡함.), 유의
    
     # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

def delete(key):
    conn = sqlite3.connect('household_Leger.db')
    
    c = conn.cursor()
    res = c.execute('''delete from ledger where serialNo = ?''',(key,)) # key - tuple 형식, 유의
    
     # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass
