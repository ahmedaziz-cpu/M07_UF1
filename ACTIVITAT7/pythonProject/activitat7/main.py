import psycopg2

from create import create_record
from read import read_records
from update import update_record
from delete import delete_record
from create_table import create_table
from connection import conn

def main():
    try:
        #creacio menu per escollir quina operació volem fer
        create_table()
        while True:
            print("\nMenú CRUD:")
            print("1. Crear registro")
            print("2. Leer registros")
            print("3. Actualizar registro")
            print("4. Eliminar registro")
            print("5. Salir")
            choice = input("Elige una opción: ")

            if choice == '1':
                campo1 = input("Campo1-Nombre: ")
                campo2 = input("Campo2-Apellido: ")
                campo3 = int(input("Campo3-Edad: "))
                campo4 = input("Campo4-Fecha de nacimiento (YYYY-MM-DD): ")
                campo5 = input("Campo5-Te gusta la naranja (True/False): ").lower() == 'true'
                campo6 = input("Campo6-Cual es tu comida favorita??: ")
                create_record(campo1, campo2, campo3, campo4, campo5, campo6)
            elif choice == '2':
                read_records()
            elif choice == '3':
                id = int(input("ID del registro a actualizar: "))
                campo1 = input("Campo1-Nombre: ")
                campo2 = input("Campo2-Apellido: ")
                campo3 = int(input("Campo3-Edad: "))
                campo4 = input("Campo4-Fecha de nacimiento (YYYY-MM-DD): ")
                campo5 = input("Campo5-Te gusta la naranja (True/False): ").lower() == 'true'
                campo6 = input("Campo6-Cual es tu comida favorita??: ")
                update_record(id, campo1, campo2, campo3, campo4, campo5, campo6)
            elif choice == '4':
                id = int(input("ID del registro a eliminar: "))
                delete_record(id)
            elif choice == '5':
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
    except (Exception, psycopg2.Error) as error:
        print("Error durante la operación:", error)
    finally:
        # Cerrar la conexión al final del programa
        if conn:
            conn.close()
            print("Conexión a la base de datos cerrada")
        #tot en bucle excepte cuan fem la 5 opcio que es sortir i tancar la connexió
if __name__ == "__main__":
    main()
