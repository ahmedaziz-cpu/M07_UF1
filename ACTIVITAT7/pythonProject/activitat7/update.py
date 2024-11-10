import psycopg2

from connection import conn

def update_record(id, campo1, campo2, campo3, campo4, campo5, campo6):
    try:
        #per fer el update lo que fem es suerposar les dades per sobre de les altres
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE my_table
            SET campo1 = %s, campo2 = %s, campo3 = %s, campo4 = %s, campo5 = %s, campo6 = %s
            WHERE id = %s
        ''', (campo1, campo2, campo3, campo4, campo5, campo6, id))
        conn.commit()
        cursor.close()
        print("Registro actualizado exitosamente")
    except (Exception, psycopg2.Error) as error:
        print("Error al actualizar el registro:", error)
