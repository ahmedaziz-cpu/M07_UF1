from connection import connect

def delete_record(record_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM mytable WHERE id = %s', (record_id,))
    conn.commit()
    cursor.close()
    conn.close()



