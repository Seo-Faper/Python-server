import sqlite3
'''
# DB 생성 (오토 커밋)
conn = sqlite3.connect("user.db", isolation_level=None)
# 커서 획득
c = conn.cursor()
# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
c.execute("CREATE TABLE IF NOT EXISTS table1 \
    (no integer PRIMARY KEY, id text, pw text, nick text)")
'''
########################test.db 파일 생#####################################
conn = sqlite3.connect("user.db", isolation_level=None)
c = conn.cursor()
c.execute("INSERT INTO table1(no, id, pw, nick) \
    VALUES(?,?,?,?)", \
    (1, 'user1','test123','김유저'))

#####################DB 테이블에 데이터 넣기##############################################
