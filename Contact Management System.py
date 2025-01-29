import re
from datetime import datetime

# Declaring the necessary variables
global countItemFounded, looping
contacts = []
countItemFounded= 0
looping = True;

def loadContacts(fileName):
    """ When the program starts, this function will load  the file and saves information that is inside the file  into the contacts list.
    It has one parameter which is the fileName and that it will be passed in function calling.
    The file will be closed autamatically after loads and parses the contacts into the contacts list"""
    global contacts
    c = 1
    try:
        #opening file as reading mode   
        with open (fileName,'r') as fName:
            dataRows = fName.read().split('\n')
                
        for values in dataRows:
            value = [v.strip() for v in values.split(",")]
            if len(value) == 6:
                contactsFromFile = {
                    'id': value[0],
                    'name': value[1],
                    'surname': value[2],
                    'DOB': value[3],
                    'mobileNo': value[4],
                    'locality': value[5]
                }
                contacts.append(contactsFromFile)
        
        fName.close()
        
    #terminate if error occur
    except FileNotFoundError:
        contacts = []
        
      
loadContacts('contacts.csv')


def saveContacts(fileName):
    """ Whe the user decides to terminate the application, this function will load  the file and saves information that is inside the contacts list  into the file.
    It has one parameter which is the fileName and that it will be passed in function calling.
    It has variable that will return false if do not any error occur.
    After saving succesfully the file will be closed"""
    global contacts
    global looping
    
    #opening file write mode
    #Loop through each contact in the contacts list
    #exception will ask a user if want to quit or  not  when IOError occur or file is only read
    try:
        with open(fileName, 'w') as fName:
            for contact in contacts:
                if isinstance(contact, dict):
                    countValue = 0
                    for key, value in contact.items():
                        if countValue < 5:
                            fName.write(value + ", ")
                        else:  
                            fName.write(value)
                        countValue += 1
                    fName.write("\n")
                else:
                    print(f"Skipping invalid contact: {contact}")

        fName.close()

    except IOError or PermissionError:
           print("The file contacts.csv is read-only or inaccessible.")
           save = input("Are you sure, you want to quit without saving any changes (y/n):  ")
           if save.lower() == 'y':
               looping = False;
               return looping
           elif save.lower() == 'n':
                looping = True;
                return looping
            
    #saving was successful
    looping = False;
    return looping

        
def showAllContacts():
    """The aim of this function is to display all contacts if a user choice become 1"""
    #display all contacts if exist else shows a message
    global contacts

    if not isinstance(contacts, list):
        print("Error: contacts is not a list.")
        return

    if not contacts:
        print("No contacts to display.")
        return

    for contact in contacts:
        if isinstance(contact, dict):
            print(f"id       :      {contact['id']}")
            print(f"name     :      {contact['name']}")
            print(f"surname  :      {contact['surname']}")
            print(f"DOB      :      {contact['DOB']}")
            print(f"mobileNo :      {contact['mobileNo']}")
            print(f"locality :      {contact['locality']}")
            print()
        else:
            print("Error: Unexpected data type in contacts!")

def addNewContact():
    """
        This function will prompt input details to the user.
        After the user enter the required information and then it will add to the contacts list
    """
    
    # Keep asking for ID until it's valid
    while True:
        idCard = input("Enter ID: ").strip()
        if validateIdCard(idCard):
            break

    name = getValidInput("Enter name: ")
    surname = getValidInput("Enter surname: ")
    dob = validateDate()
    mobileNo = validatePhoneNumber()
    locality = getValidInput("Enter locality: ")
    
    new_contact = {
            'id': idCard,
            'name': name,
            'surname': surname,
            'DOB': dob,
            'mobileNo': mobileNo,
            'locality': locality
        }
        
    if isinstance(contacts, list):
        contacts.append(new_contact)
        print("Contact added successfully!")
    else:
        print("Sorry: error ocurres while trying to add contacts.")
 

def findContactsById(idCard):
    """
    This function searches for contacts based on a provided ID.   
    Parameters:
        idCard (str): The ID to search for in the contact list.  
    Returns:
        list: A list of contacts matching the provided ID. 
              If no matches are found, it returns an empty list.
    """
    
    foundContacts = []
    
    for contact in contacts:
        if contact['id'].strip().lower() == idCard.strip().lower():
            foundContacts.append(contact)
    return foundContacts

    
def displayContactsById(contact):
    """
    This function displays the details of the contacts found.   
    Parameters:
        contact (list): A list of contacts (dictionaries) to be displayed.      
    Returns:
        None: The function prints the details of each contact and displays the total number of contacts found.
    """
    
    if not contact:
        print("No contacts found.")
        return     
    for contac in contact:
        for key, value in contac.items():
            print(key, ": " ,value)

            
def deleteContactsById(idCard):
    """
    This function deletes contacts based on the provided ID if the user confirms.
    
    Parameters:
        idCard (str): The ID of the contact to delete.
        
    It interacts with the following:
        - displayContactsById: Displays contacts matching the ID.
        - findContactsById: Finds contacts matching the ID.
    """
    
    global contacts

    # Find contacts matching the provided ID
    # Display the matching contacts  
    matching_contacts = findContactsById(idCard)
    if not matching_contacts:
        print(f"No contacts found with ID '{idCard}'.")
        return
 
    print(f"The following contact(s) match the ID '{idCard}':")
    displayContactsById(matching_contacts)
    
    # Ask the user for confirmation
    while True:
        confirmation = input("Are you sure you want to delete the above contact(s)? (y/n): ").strip().lower()
        if confirmation == 'y':
            contacts = [contact for contact in contacts if contact not in matching_contacts]
            print(f"{len(matching_contacts)} contact(s) deleted successfully.")
            break       
        elif confirmation == 'n':
            print("No contacts were removed.")
            break    
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
    

def validatePhoneNumber():
    """
    Continuously asks for a valid phone number until the user enters an 8-digit number.   
    Returns:
        str: A valid phone number.
    """
    pattern = re.compile(r'^\d{8}$')

    while True:
        phone = input("Enter mobile number (8 digits): ").strip()
        
        if pattern.match(phone):
            return phone
        else:
            print("Invalid phone number! It must contain exactly 8 digits.")

def validateDate():
    """
    Continuously asks for a valid date of birth (DOB) in DD-MM-YYYY format.   
    Returns:
        str: A valid date string.
    """
    
    date_format = "%d-%m-%Y"
    while True:
        date_str = input("Enter the DOB (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(date_str, date_format)
            return date_str
        except ValueError:
            print("Invalid date! Please enter the DOB in the format DD-MM-YYYY.")

def validateIdCard(idCard):
    """
    Validates an ID card using regex and checks if it already exists in the contacts list.
    Parameters:
        idCard (str): The ID card to validate.
    Returns:
        bool: True if valid and unique, False otherwise.
    """
    global contacts
    
    # Define regex pattern for valid ID
    # Check if the ID matches the pattern
    # Check if ID already exists in contacts
    
    pattern = r"^\d{6}[A-Z]$"
    
    if not re.match(pattern, idCard):
        print("Invalid ID format! ID must be in the format of six digits followed by an uppercase letter (e.g., '121212A').")
        return False      
    for contact in contacts:
        if contact['id'] == idCard:
            print("ID already exists in contacts. Please check the ID.")
            return False     
    return True  

def getValidInput(prompt):
    """
    Prompts the user for input and ensures it is not empty.   
    Returns:
        str: A valid non-empty input.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("This field cannot be empty.")
        
def findContactsByField(field, value):
    """Search for contacts by any field (name, surname, phone, etc.)."""
    results = []
    for contact in contacts:
        if contact[field].lower().startswith(value.lower()):
            results.append(contact)
    return results

def sortContacts(key):
    """Sort contacts by a specified key."""
    global contacts

    if not isinstance(contacts, list) or not all(isinstance(x, dict) for x in contacts):
        print("Error: contacts is not a valid list of dictionaries!")
        return
    if not all(key in contact for contact in contacts):
        print(f"Error: Key '{key}' not found in all contacts!")
        return
    
    try:
        contacts = sorted(contacts, key=lambda x: x[key].lower())
        print(f"Contacts sorted by {key}.")      
    except Exception as e:
        print("An error occurred during sorting:", e)
       
   # print("Debug: Current state of contacts before sorting:", contacts)

def getMenuChoice():
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
def mainCode():
    """
    This function serves as the main menu for the Contact Manager program.
    
    It repeatedly displays a menu allowing the user to:
        1. Show all contacts
        2. Add a new contact
        3. Find a contact by ID
        4. Delete a contact by ID
        5. Sort contacts
        6. Quit and save contacts
    
    The function ensures user input is valid and handles errors gracefully.
    """
  
    while looping:
        print("========================================")
        print("        Welcome to Contact Manager      ")
        print("========================================")
        print("1 - Show all contacts")
        print("2 - Add new contact")
        print("3 - Find contact")
        print("4 - Delete contact")
        print("5 - Sort contacts")
        print("6 - Quit")
        
        try:
            userChose = int(input("Enter your choice:  ").strip())

            match userChose:
                case 1:
                    print("Item 1 selected: Show all contacts")
                    showAllContacts()
                case 2:
                    print("Item 2 selected: Add new contact")
                    addNewContact()
                case 3:
                    print("Item 3 selected: Find contact")
                    idCard = input("Enter the ID of the contact: ").strip()
                    displayContactsById(findContactsById(idCard))
                case 4:
                    print("Item 4 selected: Delete contact")
                    idCard = input("Enter the ID of the contact: ").strip()
                    deleteContactsById(idCard)
                case 5:
                    print("Item 5 selected: Sort contacts")
                    sortKey = input("Sort by (name, surname, locality): ").strip().lower()
                    if sortKey in ['name', 'surname', 'locality']:
                        sortContacts(sortKey)
                    else:
                        print("Invalid sort key. Please enter 'name', 'surname', or 'locality'.")
                case 6:
                    confirm_exit = input("Are you sure you want to exit? (y/n): ").strip().lower()
                    if confirm_exit == 'y':
                        saveContacts('contacts.csv')
                        print("Contacts saved successfully. Exiting...")
                        break
                    else:
                        print("Returning to the main menu...")
                case _:
                    print("Invalid input! Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Saving contacts before exiting...")
            saveContacts('contacts.csv')
            print("Contacts saved successfully. Exiting...")
            break

try:
    mainCode()
except ValueError:
    print(f"An unexpected error occurred: {e}")
    print("Exiting the program...")
    saveContacts('contacts.csv')
    print("Contacts saved successfully. Application exiting.")
   
