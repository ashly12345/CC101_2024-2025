def record_keeper():
    records = {}

    while True:
        print("\nChoose an option:")
        print("a. Add data")
        print("b. Delete data")
        print("c. End")
        choice = input("Enter your choice (a/b/c): ").strip().lower()

        if choice == 'a':
            key = input("Enter key: ")
            value = input("Enter value: ")
            records[key] = value
            print("Record added:", records)

        elif choice == 'b':
            key = input("Enter key to delete: ")
            if key in records:
                del records[key]
                print("Record deleted:", records)
            else:
                print("Key not found.")

        elif choice == 'c':
            print("THANK YOU")
            break

        else:
            print("Invalid choice. Please choose a, b, or c.")

if __name__ == "__main__":
    record_keeper()

























