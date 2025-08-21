import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if name in contacts:
        print("⚠️ Contact already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print("✅ Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"{name} -> Phone: {info['phone']}, Email: {info['email']}")
    print("-------------------")

# Search a contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"🔎 Found: {name} -> Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("❌ Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("🗑️ Contact deleted successfully!")
    else:
        print("❌ Contact not found.")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    main()

