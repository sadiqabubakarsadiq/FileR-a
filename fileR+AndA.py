#program to allow user to create, read, and write
#to a file and  append text to it

#importing FileR+ and a_Tools module for functions usage
import tools

#main menu function
def menu():
    listOfPrompts = ["Welcome to FileR+ And a",
                     "Choose an option from the below list of prompts",
                     "1-Instructions",
                     "2-Do with files",
                     "3-About Us"]
    for prompts in listOfPrompts:
        print(prompts)
    choice = ""
    while choice != "1" and choice != "2" and choice != "3":
        choice = input("Enter section number: ")
        if choice == "1":
            tools.instructons()
        elif choice == "2":
            tools.doWithFiles()
        elif choice == "3":
            tools.aboutUs()
        else:
            print("Invalid Selection")


menu()