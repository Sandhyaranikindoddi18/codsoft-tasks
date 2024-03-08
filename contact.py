import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        # Labels and Entry widgets
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_entry = tk.Entry(self.root)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(self.root, width=50, height=10)
        self.contact_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Grid layout
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button.grid(row=2, column=0, pady=10)
        self.view_button.grid(row=2, column=1, pady=10)
        self.delete_button.grid(row=3, column=0, pady=10)
        self.search_button.grid(row=3, column=1, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone}
            self.contacts.append(contact)

            messagebox.showinfo("Success", "Contact added successfully!")

            # Clear entry fields
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Please enter both name and phone number.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)  # Clear existing entries

        if not self.contacts:
            messagebox.showinfo("Empty", "No contacts available.")
        else:
            for contact in self.contacts:
                self.contact_listbox.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()

        if selected_index:
            selected_index = int(selected_index[0])
            deleted_contact = self.contacts.pop(selected_index)
            self.contact_listbox.delete(selected_index)
            messagebox.showinfo("Contact Deleted", f"Contact '{deleted_contact['Name']}' deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def search_contact(self):
        search_name = self.name_entry.get()

        if not search_name:
            messagebox.showwarning("Warning", "Please enter a name to search.")
            return

        matching_contacts = [contact for contact in self.contacts if search_name.lower() in contact['Name'].lower()]

        self.contact_listbox.delete(0, tk.END)  # Clear existing entries

        if matching_contacts:
            for contact in matching_contacts:
                self.contact_listbox.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")
        else:
            messagebox.showinfo("No Matches", "No contacts found matching the search criteria.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()


