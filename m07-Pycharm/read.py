from connection import connect

def read_records():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mytable')
    records = cursor.fetchall()
    for record in records:
        print(record)
    cursor.close()
    conn.close()



