#fileR+ and a functions module
def instructons():
    tellThem = ["Instructions/GuideLines",
                "Follow the following guidelines for easy setups",
                "1-In the menu functions you are required to select an option from the listed options and select it with it's index no",
                "2-In the instruction sections it's give you guidelines",
                "3-In the Do with files section, you can select what you want to do either create a file write/over write to it, read, and append text to a file",
                "3-The About Us section tells you about the developer of the app"
                ]
    #for loop to loop through tellThem list
    for listThem in tellThem:
        print(listThem)
    goTo()#funtion to take us to a specific section

def doWithFiles():
    doWithFilesOptions = ["Do With Files",
                          "Choose or select an option from the following\
with their index no",
                          "1-Create File",
                          "2-Create/write file",
                          "3-Read file",
                          "4-Append Text to a file"]
    # for loop to loop through doWithFilesOptions list and take input
    for fileOptions in doWithFilesOptions:
        print(fileOptions)
    inputFileOption = ""
    #while loop to prompt user for input aslong as his input is invalid
    while inputFileOption != "1" and inputFileOption != "2" and inputFileOption != "3" and inputFileOption != "4":
        inputFileOption = input("Enter your option: ")
        if inputFileOption == "1":
            createFile()
        elif inputFileOption == "2":
            writeToFile()
        elif inputFileOption == "3":
            readFile()
        elif inputFileOption == "4":
            print("append Text To a file")
        else:
            print("Selection invalid")

def aboutUs():
    aboutUsMe = ["This app was developed by Sadiq Abubakar Sadiq, CEO of SASapps and www.MVPNSAS.com",
                 "He is a software engineer by self taught and also a PYTHON and C++ programmer.",
                 "He have develop differents apps some of them includes:JavaScript Quiz Questions, Friends Guess, Math Calc etc",
                 "FileR+ and A to make it easy for people to create, read and write files",
                 "For any complain or advice contact me through my Email or website",
                 "Email:SASappssupport3576@gmail.com",
                 "website:www.SASapps,inc.com",
                 "All right reserve",
                 "Copyright © 2018-2019"
                 ]
    for tellAboutUs in aboutUsMe:
        print(tellAboutUs)
    goTo()#function to take user to a specific section

#function to allow user to create a new file
def createFile():
    FILENAME = input("Enter file name to be created with it's extension: ")
    FILEMODE = "w"
    #opening the file which is equivalent to create = open(FILENAME, FILEMODE)
    with open(FILENAME, FILEMODE) as create:
        #closing the file
        create.close()
    print(FILENAME + " Created successfully")
    goTo()

#function to allow user to write to a file
def writeToFile():
    FILENAME = input("Enter file name to write to, with it's extension: ")
    FILEMODE = "w"
    textToWrite = input("Enter text to write to file: ")
    #opening the file which is equivalent to create = open(FILENAME, FILEMODE)
    with open(FILENAME, FILEMODE) as write:
        write.write(textToWrite)
    write.close()
    print(textToWrite + " have been successfully been written to " + FILENAME)
    goTo()

#function to read text from file
def readFile():
    FILENAME = input("Enter file name to read from, with it's extension: ")
    FILEMODE = "r"
    readFromFile = open(FILENAME, FILEMODE)
    #loop to loop through file
    for read in readFromFile.readlines():
        print(read)
    readFromFile.close()
    print(FILENAME + " Readed successfully")
    goTo()

#function to allow user to append text to a file
def appendTextToFile():
    FILENAME = input("Enter file name to append text to the file: ")
    FILEMODE = "a"
    textToappend = ""
    addTextToFile = open(FILENAME, FILEMODE)

    while textToappend != "-1":
        textToappend = input("Enter a text and press enter to continue to next line or -1 to save: ")
        if textToappend != "-1":
            addTextToFile.write("\n" + textToappend)
        elif textToappend == "-1"


#goto function to take user to a specific section
def goTo():
    takeTo = ""
    goToCommands = ["Here is a list of command to use to goto a specific section",
                    "I - to goto instructions section",
                    "DWF - to goto Do With Files section",
                    "AU - to goto About Us section"]
    for takeToCmd in goToCommands:
        print(takeToCmd)
    while takeTo != "I" and takeTo != "DWF" and takeTo != "AU":
        takeTo = input("Enter a command: ").upper()
        if takeTo == "I":
            instructons()
        elif takeTo == "DWF":
            doWithFiles()
        elif takeTo == "AU":
            aboutUs()
        else:
            print("There is no such command " + takeTo)