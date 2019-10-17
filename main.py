
# ###################### Introduction #############################
#                                                                 #
#    #Name: Sijan Malla              Date Assigned:Sept. 24,2019  #
#    #                                                            #
#    #Course: 2000-44306             Date Due : Oct. 1, 2019      #
#    #                                                            #
#    #File name: Programming Assignment 4                         #
#    #                                                            #
#    #Program Description: It acts as a webiste for a amusement   #
#                          park for selling the tickets.          #
#                                                                 #
##################### Program Begins ##############################


#Formatting Title of Program
print()
print("{0:^60s}".format("=-"*20))
print()
print("{0:^60s}".format("DECODE MESSAGES HERE!"))       #Title of the Programming
print()
print("{0:^60s}".format("=-"*20))
print()
print("="*60)


userChoice = "y"        #Predefining the value of userChoice as "y" so that the progam executes on its own for first choice.

# Whole Program Body Begins
while userChoice == "y":        #Looping for if user wants to run the program again. For this user must input userChoice as "y".

    print()

    fileName = input("Enter encoded file name: ")       #asking user for the name of encoded file.

    while not(".txt" in fileName):      #input validation for ensuring that the given file must be a .txt format
        fileName = input("Error! Enter encoded file name (only .txt format is accepted): ")

    print()
    print()

    #Formatting for display of  "DECODED MESSAGE"
    style = "+"+"-"*17+"+"
    print("{0:^58s}".format(style))
    print(" "*2+"-"*17+"|"+" DECODED MESSAGE "+"|"+"-"*19)
    print("{0:^58s}".format(style))

    print()
    print()


    #Opening up the file to DECODE using File Handling in Python
    fileToDecode= open(fileName,"r")        #Given encodde file is opened in read mode and stored as fileToDecode

    forInnerLoop = ""       #Declaring variable to be used inside the for everySentence loop.
    decodedSentence=""             #Declaring variable to be used inside the for everyCharacter Loop.

    for everySentence in fileToDecode:      #For loop to run until there is sentence in a given file. It reads each lines in single loop.
        LineInFile = each.rstrip()      #LineInFile is used to store each lines one at a time so as to pass its value to inner for everyCharacter Loop.

        for everyCharacter in LineInFile:       #For loop to run until there is character in a given line. It reads each charcter in single loop.

            if not(everyCharacter==" "):     #To check if given character is space i.e. word seperator. Since, we don't want to use any other character as word seperator. If true ie. given character is not " " it executes.

                encodedCharToASCII = ord(everyCharacter)     #ASCII value of encoded character

                ASCIIForDecodedCharacter = encodedCharToASCII + 2       #Since message has been encoded by subtracting characters ascii value by 2. So we do reverse that is add 2 to decode the encoded message.

                entence+= chr(ASCIIForDecodedCharacter)        #Accumulating character one after another in its decoded form

            else:
                decodedSentence+=" "       #It is to ignore the fact that we want space to be the word seperator but not any other charater. so, if space character is detected we leave it as it is.

        print(decodedSentence)     #To print the single linee of the decoded message from the encoded message

        decodedSentencesentence=""     #Resetting the value for sentence to zero so that when new line is read from outer loop the values for earlier sentence in deleted from the variable "sentence"

    fileToDecode.close()        #To stop reading from input encoded text file

    print()

    style = "+"+"-"*17+"+"
    print("{0:^58s}".format(style))
    print(" "*2+"-"*17+"|"+"  END OF MESSAGE "+"|"+"-"*19)
    print("{0:^58s}".format(style))
    print()

    print()
    print()
    userChoice = input("Would you like to decode another file(y/n)?: ")
    userChoice = userChoice.lower()
    while not(userChoice == "y" or userChoice == "n"):
        userChoice = input("Error! Enter your choice(y and n are only allowed): ")

print()
print("Thank you for using our program. Please come again!")
