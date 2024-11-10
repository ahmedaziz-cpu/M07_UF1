import psycopg2

from connection import conn

def read_records():
    try:
        #Per llegir tots els registres lo que hem de fer es una consulta,i guardar-la
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM my_table')
        records = cursor.fetchall()
        for record in records:
            print(record)
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error al leer los registros:", error)
