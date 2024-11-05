from connection import connect

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mytable (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER,
            email VARCHAR(100),
            city VARCHAR(100),
            country VARCHAR(100)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_table()



