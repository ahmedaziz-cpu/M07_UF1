import psycopg2

from connection import conn

def create_record(campo1, campo2, campo3, campo4, campo5, campo6):
    try:
        #Fem un insert que seria posar tottes les dades ,i posar-les on corresonen i el seu tipus o valor
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO my_table (campo1, campo2, campo3, campo4, campo5, campo6)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (campo1, campo2, campo3, campo4, campo5, campo6))
        conn.commit()
        cursor.close()
        print("Registro creado exitosamente")
    except (Exception, psycopg2.Error) as error:
        print("Error al crear el registro:", error)
