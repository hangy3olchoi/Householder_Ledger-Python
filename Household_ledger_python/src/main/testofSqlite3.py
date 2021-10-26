'''
Created on 2021. 7. 22.

Sqlite3의 사용 기초

@author: pc356
'''

import sqlite3

print(sqlite3.version)

# 1단계 - Connection 객체 얻기
# 'isolation_level = None'를 지정하는 이유는 데이타베이스에 자동 커밋하기 위해
conn = sqlite3.connect('household_Leger.db', isolation_level = None) # 확장자를 반드시 .db로 줘야함, 'isolation_level = None' 생략 가능

# 2단계 - cursor 획득단계
cursor = conn.cursor()

# 3단계 - table 만들기(이미 완성된 것을 끌어쓸 수 있다.)
# TEXT(문자열), NUMERIC(숫자), INTEGER(정수), REAL(실수), BLOB(대용량 바이너리 정보 - 이미지) 등의 타입이 존재.
cursor.execute('''
    create table if not exists testTable
    (serialNo text primary key,
     date text,
     section text,
     title text,
     revenue text,
     expense text,
     remark text)
''') # 'testTable'이라는 테이블이 존재 하지 않는다면 '항목 타입 프라이머리키(해당될 경우),' 의 형식으로 입력 

# isolation_level = None가 없다면 아래의 과정을 반드시 수행.
# conn.commit() - isolation_level = None으로 지정되었기 때문 커밋이 필요없음
# cursor.close()
# conn.close()

