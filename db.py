import sqlite3

########################test.db 파일 생성#####################################
'''
# DB 생성 (오토 커밋)
conn = sqlite3.connect("user.db", isolation_level=None)
# 커서 획득
c = conn.cursor()
# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
c.execute("CREATE TABLE IF NOT EXISTS table1 \
    (no integer PRIMARY KEY, id text, pw text, nick text)")
'''
##################### DB 테이블에 데이터 넣기(INSERT) #########################
'''
conn = sqlite3.connect("user.db", isolation_level=None)
c = conn.cursor()
c.execute("INSERT INTO table1(no, id, pw, nick) \
    VALUES(?,?,?,?)", \
    (2, 'user2','test234','박유저'))
'''
##################### 데이터  전체 조회 ############################################

'''
conn = sqlite3.connect("user.db", isolation_level=None)
c = conn.cursor()

c.execute("SELECT * FROM table1")

print(c.fetchall())
input()
'''
################### 조건 순회 1 ##########################################

conn = sqlite3.connect("user.db", isolation_level=None)
c = conn.cursor()

param1 = (2,)
c.execute('SELECT * FROM table1 WHERE id=?',param1)
print(c.fetchone())
input()
