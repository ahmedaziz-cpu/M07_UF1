import psycopg2

try:
    # Intentar conectar a la base de datos
    conn = psycopg2.connect(
        dbname="db",
        user="ahmed",
        password="ahmed",
        host="localhost",
        port="5432"
    )
    print("Conexión exitosa a la base de datos")

    # Crear un cursor
    cursor = conn.cursor()
    print("Cursor creado:", cursor)

except (Exception, psycopg2.Error) as error:
    print("Error al conectar a la base de datos:", error)
