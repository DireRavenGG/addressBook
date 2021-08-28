# address book 
#   - store a name and a corresponding phone number (can be in plain 10 digits)
#       and an email address (lastname.firstname@email.com)
#   - functions to build
#       list -- list all entries in the address book
#       add -- add an entry
#       delete -- delete an entry
#       search -- find an entry based on given name
#       save -- save changes to the address book file
#       close -- close the address book


addressBook = []

def openFile():
    try:
        writer = open("./addressBook/addressBook.txt", "r")
        addressBook.append(writer.readlines())
    except:
        new = open("./addressBook/addressBook.txt", "x")
        addressBook.append(new)

openFile()

def addInfo(): # add entry
    phoneNumber = str(input("Please input phone number: "))
    firstName = input("Please input first name: ").strip().capitilize()
    lastName = input("Please input last name: ").strip().capitilize()
    email = input("Please input email address: ").strip().lower()
    contact = (firstName, lastName, phoneNumber, email)
    addressBook.append(contact)
    
def listDirectory(): # list all entrys
    print(addressBook )

def searchDirectory():
    firstName = input("Input name you are searching for: ").lower()
   
    for item in addressBook:
        if firstName == item[0]:
            print(item)

def deleteEntry():
    firstName = input("Input name you are looking to delete: ").lower()

    for item in addressBook:
        if firstName == item[0]:
            addressBook.remove(item) 

def helpCommand():
    print("Command list: help, add, list, search, delete, save and close.")

def saveDirectory(): 
    writer = open("./addressBook/addressBook.txt", "w")
    writer.write("%s" % addressBook)
    print("|||SAVING|||")
    writer.close()

while True:
    commands = input("Type help for list of commands. Please enter command:  ")
    if commands == "add":
        addInfo()
    elif commands == "list":
        listDirectory()
    elif commands == "search":
        searchDirectory()
    elif commands == "delete":
        deleteEntry()
    elif commands == "help":
        helpCommand()
    elif commands == "save":
        saveDirectory()
    elif commands == "close":
        break