class RecordKeepingApp:
    def __init__(self):
        self.records = []

    def add_data(self):
        record = input("Enter the record to add: ")
        self.records.append(record)
        print(f"Record '{record}' added.")

    def delete_data(self):
        record = input("Enter the record to delete: ")
        if record in self.records:
            self.records.remove(record)
            print(f"Record '{record}' deleted.")
        else:
            print(f"Record '{record}' not found.")

    def display_records(self):
        if not self.records:
            print("No records found.")
        else:
            print("Current Records:")
            for record in self.records:
                print(f"- {record}")

    def run(self):
        while True:
            print("\nRecord Keeping App")
            print("1. Add Data")
            print("2. Display Data")
            print("3. Delete Data")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.add_data()
            elif choice == '2':
                self.display_records()
            elif choice == '3':
                self.delete_data()
            elif choice == '4':
                print(" Goodbye! Thank You!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = RecordKeepingApp()
    app.run()
