import os

# File to store birthday data
FILE_NAME = "birthdays.txt"

# Load existing birthdays from file
birthdays = {}

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                name = parts[0].strip()
                date = parts[1].strip()
                birthdays[name] = date

def save_birthdays():
    with open(FILE_NAME, "w") as file:
        for name, date in birthdays.items():
            file.write(f"{name}:{date}\n")

def show_menu():
    print("\n--- Birthday Tracker ---")
    print("1. Add Birthday")
    print("2. View All Birthdays")
    print("3. Find Birthday by Name")
    print("4. Exit")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        entry = input("Enter name and birthday (e.g., John 15/08/2005): ")
        parts = entry.split()
        if len(parts) == 2:
            name, bday = parts[0], parts[1]
            birthdays[name] = bday
            save_birthdays()
            print(f"✅ Birthday for {name} added.")
        else:
            print("❌ Invalid format. Please enter: Name DD/MM/YYYY")

    elif choice == '2':
        if birthdays:
            print("\n🎂 Stored Birthdays:")
            for name in sorted(birthdays):
                print(f" - {name} : {birthdays[name]}")
        else:
            print("📂 No birthdays stored yet.")

    elif choice == '3':
        name = input("Enter the name to search: ")
        if name in birthdays:
            print(f"🎉 {name}'s birthday is on {birthdays[name]}")
        else:
            print("❌ Name not found.")

    elif choice == '4':
        print("👋 Exiting Birthday Tracker. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter 1-4.")
