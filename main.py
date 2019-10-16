
# ###################### Introduction #############################
#                                                                 #
#    #Name: Sijan Malla              Date Assigned:Sept. 24,2019  #
#    #                                                            #
#    #Course: 2000-44306             Date Due : Oct. 1, 2019      #
#    #                                                            #
#    #File name: Programming Assignment 2                         #
#    #                                                            #
#    #Program Description: It acts as a webiste for a amusement   #
#                          park for selling the tickets.          #
#                                                                 #
##################### Program Begins ##############################
'''
#Title of Program
print()
print("{0:^60s}".format("=-"*20))
print()
print("{0:^60s}".format("DECODE MESSAGES HERE!"))
print()
print("{0:^60s}".format("=-"*20))
print()
print("="*60)
print()

#Taking fileName from the user
fileName = input("Enter encoded file name: ")
print()
print()

#To Display Title "DECODED MESSAGE"
style = "+"+"-"*17+"+"
print("{0:^58s}".format(style))
print(" "*2+"-"*17+"|"+" DECODED MESSAGE "+"|"+"-"*19)
print("{0:^58s}".format(style))
print()

print()
'''
#Opening up the file to DECODE
fileToDecode= open(fileName,"r")
forInnerLoop = ""
sentence=""
for each in fileToDecode:
    forInnerLoop = each.rstrip()
    for a in forInnerLoop:
        if not(a==" "):
            decodedchartoASCII = ord(a)
            realValueForASCII = decodedchartoASCII + 2
            sentence+= chr(realValueForASCII)
        else:
            sentence+=" "
    print(sentence)
    sentence=""
fileToDecode.close()
