# Contact Management System
A Python-based contact management system that allows users to manage a list of contacts. The application supports loading contacts from a file, adding new contacts, searching for contacts by name, displaying all contacts, and deleting contacts.

This project demonstrates Python programming concepts and file handling, and serves as a learning tool for developing CLI-based applications.

## Features
- **Load Contacts:** Automatically loads contacts from a CSV file at startup.
- **Save Contacts:** Saves all contact details into a CSV file when exiting.
- **Display All Contacts:** View a list of all stored contacts.
- **Add New Contact:** Add a new contact with details such as name, surname, date of birth, mobile number, and locality.
- **Find Contacts:** Search for a contact by name and display the details.
- **Delete Contacts:** Remove contacts by name after confirmation.

## Project Structure
- **loadContacts(fileName):** Reads and loads contact data from a CSV file into a list.
- **saveContacts(fileName):** Saves the current list of contacts back into a CSV file.
- **showAllContacts():** Displays all stored contacts.
- **addNewContact():** Prompts the user to input and add a new contact to the list.
- **findContactsByName(name):** Searches for a contact by name and returns matches.
- **deleteContactsByName(name):** Deletes a contact by name after user confirmation.
- **mainCode():** The main menu-driven interface for interacting with the system.

## Getting Started
### Prerequisites
- Python 3.x installed on your system.
### Setup
1. Clone the repository:
   https://github.com/ZamirLucky/contact-management-system-used-python.git
2. make sure the contacts.csv file to place in the same directory as the script.

## Technologies Used
- Python (CLI-based application)
- File handling for reading and writing CSV files

## Future Improvements
- Add GUI support for better usability.
- save the contacts to database
- Enhance search functionality.
- Add filter functionality. 


