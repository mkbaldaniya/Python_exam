import os
import datetime

class Journal:
    def __init__(self):
        self.filename = "journal.txt"
        self.separator = "-" * 40

    def add_entry(self):
        how_entry = int(input("enter How many entry add :"))
        for i in range(how_entry):

            print("\n--- Add a New Entry ---",i+1)
            entry_content = input("Enter your journal entry: ")
            
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                with open(self.filename, 'a') as file:
                    file.write(f"[{timestamp}]\n")
                    file.write(f"{entry_content}\n")
                    file.write(f"{self.separator}\n")
                print("Entry added successfully!\n")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def view_entries(self):
        print("\n--- View All Entries ---")
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                if not content:
                    print("The journal is empty.")
                else:
                    print("Your Journal Entries:")
                    print(self.separator)
                    print(content)
        except FileNotFoundError:
            print("Output: No journal entries found. Start by adding a new entry!")
        except PermissionError:
            print("Error: Permission denied. Unable to read file.")

    def search_entries(self):
        print("\n--- Search for an Entry ---")
        keyword = input("Enter a keyword or date to search: ")
        
        if not keyword:
            print("Please enter a valid keyword.")
            return

        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            entries = content.split(self.separator)
            
            found_entries = []
            for entry in entries:
                if keyword.lower() in entry.lower():
                    if entry.strip():
                        found_entries.append(entry.strip())
            
            if found_entries:
                print("\nOutput: Matching Entries:")
                print(self.separator)
                for entry in found_entries:
                    print(entry)
                    print(self.separator)
            else:
                print(f"Output: No entries were found for the keyword: '{keyword}'.")
                
        except FileNotFoundError:
            print("Error: The journal file does not exist yet.")

    def delete_entries(self):
        print("\n--- Delete All Entries ---")
        confirm = input("Are you sure you want to delete all entries? (yes/no): ").lower()
        
        if confirm == 'yes':
            try:
                if os.path.exists(self.filename):
                    os.remove(self.filename)
                    print("Output: All Journal entries have been deleted.")
                else:
                    print("Output: No journal entries to delete (file does not exist).")
            except PermissionError:
                print("Error: Permission denied. Unable to delete file.")
            except Exception as e:
                print(f"Error: Could not delete file. {e}")
        else:
            print("Deletion cancelled.")


j1 = Journal()
    
while True:
    print("Welcome to Personal Journal Manager!")
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
        
    choice = int(input("User Input: "))
    match choice:
        case 1:
            j1.add_entry()

        case 2:
            j1.view_entries()

        case 3:
            j1.search_entries()

        case 4:
            j1.delete_entries()

        case 5:
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break

        case _:
            print("Invalid option. Please select a valid option from the menu.")
    