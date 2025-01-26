# Declaring the necessary variables
global contacts, countItemFounded, looping
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
        #---------------- opening file as reading mode
     
        with open (fileName,'r') as fName:
            dataRows = fName.read().split('\n')
                
        for values in dataRows:
            value = values.split(",")
            if len(value) == 5:
                contactInfo = {'name':value[0],'surname':value[1],'DOB':value[2],'mobileNo':value[3],'locality':value[4]}
                contacts.append(contactInfo)
        print(contacts)
        fName.close()
    #Application will terminate if error occur
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

    # ------------------------Trying to open the file 
    try:
        #opening file write mode
        fName = open(fileName,'w')

#--------------------------------------------------Saving contacts list into the file 
        for contacts in contacts:
            countValue = 0
            for key, value in contacts.items():
                newLine = False
                line = ""
                if countValue <= 3:
                    line = value+ ", "
                    fName.write(line)
                elif countValue == 4:
                    line = value
                    fName.write(line)
                    newLine = True
                if newLine == True:
                    line = "\n"
                    fName.write(line)
                    countValue = 0
                    continue
                countValue += 1
        fName.close()

 #-------------------Application will ask a user if want to quit or  not  when IOError occur or file is only read
    except IOError or PermissionError:
           print("The file contacts.cvs is only read..")
           save = input("Are you sure, you want to quit without saving any changes (y/n)  ")
           if save.lower() == 'y'.lower():
               looping = False;
               return looping
               fName.close()
           elif save.lower() == 'n'.lower():
                looping = True;
                return looping
    looping = False;
    return looping

        


def showAllContacts():
    """The aim of this function is to display all contacts if a user choice become 1"""
    #--------------------- for loop will display all contacts if exist else shows a message
    global contacts
    countThisItems = 1
    if contacts:
        #loop for contacts list 
        for contacts in contacts:
            #loop for the dict in list
            for keys, values in contacts.items():
                print(keys, ":          ",values)
                if countThisItems == 5:
                    print()
                    countThisItems = 1
                    continue
                countThisItems += 1
    else:
        print("list is empty..")

def addNewContact():
    """ This function will prompt input details to the user.
        After the user enter the required information and then it will add to the contacts list """
    #-------------------------user required to input expected details and then adds to the  list  
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    DOB = str(input("Enter DOB: "))
    mobileNo = input("Enter mobileNo: ")
    locality = input("Enter locality: ")
    contactInfo = { 'name':name, 'surname':surname, 'DOB':DOB,'mobileNo':mobileNo,'locality':locality}
    contacts.append(contactInfo)

def findContactsByName(name):
    """This function prompts the user to enter a name to find a maching contacts.
        It has one parameter which is the name and that it will be passed in function calling as user prompt.
        The function will return the founded contact(s) as a list."""
    foundLists = []
    #----------------------for loop that checks  if inputed name found in list and then returns a list of name(s) else diplsys a message
    for d in contacts:
        if d ['name'].lower() == name.lower():
            foundLists.append(d)
        else:
            print("No contacts were found with name",name)

           
    return foundLists 


def displayContactsByName(name):
    """This function will display if the contcats founded or not .
        It has one parameter which is the name and that it will be passed in the function calling as another function which is findContactsByName.
        The function will return as the value of  name."""
    #----- displaying the founded contacts   
    c = 0
    global countItemFounded
    countItemFounded = 0
    for name in name:
        for keys, values in name.items():
            print(keys,":     " ,values)
            if c == 4:
                countItemFounded+=1
                print()
                c = 0
                continue
            c+=1
            
    print(countItemFounded,"contacts found..")
    return

def deleteContactsByName(name):
    """This function will be deleted the contcats  if the user agree  .
        It has one parameter which is the name and that it will be passed in the function calling
        which is two another functions displayContactsByName and findContactsByName."""
    global contcats
    # ---- asking a user to make sure if decide to delete the contacts
    print("Are you sure you want to remove the above ",count,"contact(s)  (y/n)?  ")
    deleteName = input()
    if deleteName.lower() == 'y'.lower():
        print("conatcts deleted")
    elif deleteName.lower() == 'n'.lower():
        print("not contacts were removed")
    else:
        print("you should enter y/n")
    
def mainCode():
    """ This function will display the main program  and this is my extra function"""
  
    while(looping == True):
        print("---------------------------\nMain Menu\n----------------------------")
        print("1 - Show all contcats\n2 - Add new contact\n3 - Find contact\n4 - Delete contact\n5 - Quit")
        userChose = int(input("Enter your choice:  "))

        if userChose == 1:
            print("Item 1 was selected:  see contacts")
            showAllContacts()
        elif userChose == 2:
            print("Item 2 was selected:  Add new contact")
            addNewContact()
        elif userChose == 3:
            print("Item 3 was selected:  find contact")
            displayContactsByName(findContactsByName(input("Enter the first name of the contacts: ")))
        elif userChose == 4:    
            print("Item 4 was selected:  delete contact")
            deleteContactsByName(displayContactsByName(findContactsByName(input("Enter the first name of the contacts: "))))
        elif userChose == 5:
            print("Saving contacts and exiting....")
            saveContacts('contacts.csv')         
        else:
            print("Please enter a number between 1 and 5...")


try:
    mainCode()
except ValueError:
    print("Please enter a number between 1 and 5")
    try:
        mainCode()
    except ValueError:
        print("Please enter next time only digits between 1 and 5..Application Exciting.... ")
   
