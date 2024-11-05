from create import create_record
from read import read_records
from update import update_record
from delete import delete_record
from create_table import create_table

def menu():
    print("1. Create record")
    print("2. Read records")
    print("3. Update record")
    print("4. Delete record")
    print("5. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            city = input("Enter city: ")
            country = input("Enter country: ")
            create_record(name, age, email, city, country)
        elif choice == '2':
            read_records()
        elif choice == '3':
            record_id = int(input("Enter record ID to update: "))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            city = input("Enter city: ")
            country = input("Enter country: ")
            update_record(record_id, name, age, email, city, country)
        elif choice == '4':
            record_id = int(input("Enter record ID to delete: "))
            delete_record(record_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



