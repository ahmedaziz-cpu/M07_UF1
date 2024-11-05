from connection import connect

def update_record(record_id, name, age, email, city, country):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE mytable
        SET name = %s, age = %s, email = %s, city = %s, country = %s
        WHERE id = %s
    ''', (name, age, email, city, country, record_id))
    conn.commit()
    cursor.close()
    conn.close()



