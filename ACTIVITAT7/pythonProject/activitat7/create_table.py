from connection import conn
import psycopg2

def create_table():
    try:
        cursor = conn.cursor()
        #Creem la taula i diem el tipus amb el cual volem aquest valor
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS my_table (
                id SERIAL PRIMARY KEY,
                campo1 VARCHAR(50),
                campo2 VARCHAR(50),
                campo3 INTEGER,
                campo4 DATE,
                campo5 BOOLEAN,
                campo6 TEXT
            )
        ''')
        conn.commit()
        cursor.close()
        print("Tabla creada exitosamente")
    except (Exception, psycopg2.Error) as error:
        print("Error al crear la tabla:", error)

if __name__ == "__main__":
    create_table()








