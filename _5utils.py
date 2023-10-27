import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='Learn@9998',
    database='mysql',
    host='localhost',
    port='3306'
)
# with conn.cursor() as c:
#     c.execute('use bank')
#     c.execute('alter table bank_accounts modify column Balance decimal(20, 2)')
#     conn.commit()
# conn.close()


