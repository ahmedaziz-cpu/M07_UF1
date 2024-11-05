from connection import connect

def create_record(name, age, email, city, country):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO mytable (name, age, email, city, country)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, age, email, city, country))
    conn.commit()
    cursor.close()
    conn.close()



