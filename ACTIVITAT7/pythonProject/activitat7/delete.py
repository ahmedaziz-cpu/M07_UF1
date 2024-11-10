import psycopg2

from connection import conn

def delete_record(id):
    try:
        #Per eliminar la fila lo que s'ha de fer es posar el delete i dir la taula i id que volem eliminar
        cursor = conn.cursor()
        cursor.execute('DELETE FROM my_table WHERE id = %s', (id,))
        conn.commit()
        cursor.close()
        print("Registro eliminado exitosamente")
    except (Exception, psycopg2.Error) as error:
        print("Error al eliminar el registro:", error)
