# docker上のmysqlにホストのpythonから接続する方法
# 事前に、sample_db上に、id列を持つtestというテーブルを作成し、id=1のデータをinsertしておく。
# create table test(id int(10));
# insert into test values(1);

import pymysql.cursors

conn = pymysql.connect(host='localhost',
                    user='root',
                    password='password',
                    db='sample_db',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM test where id = %s"
        cursor.execute(sql, ('1',)) 
        result = cursor.fetchall()
        print(result)
finally:
    conn.close()
    
print(result)