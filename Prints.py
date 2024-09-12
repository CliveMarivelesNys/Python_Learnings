import ArrayEditer
import GuesstheWord
import StudentDatabase
import StudentEnrollment
from Database import *


def OptionsMenu():
    print("""
    Welcome to Clive's project hud
    To start here are the current projects you can access
    
    1) Grocery List
    2) Splicing Word
    3) Lessons
    4) Greater or Less than
    5) Student Database
    6) Guess the Word
    7) Array Editor
    8) Student Enrollment
    0) Exit Program
    """)

    choice = int(input("    Enter project you want to access: "))

    if choice == 1:
        print('grocery list')
        GroceryListMenu()

    elif choice == 2:
        print('splicing list')
        outputcombinedword()
    elif choice == 3:
        print('Lessons')
    elif choice == 4:
        print('Greater or Less than')
        greaterorlessthan()
    elif choice == 5:
        print('Student Database')
        StudentDatabase.database_interface()
    elif choice == 6:
        print("Random word guesser")
        GuesstheWord.guess_interface()
    elif choice == 7:
        print("Array Editor")
        ArrayEditer.interface_arrayediter()
    elif choice == 8:
        print("Student Database")
        StudentEnrollment.interface_studentenrollment()
    elif choice == 0:
        print('Exiting Program')
    else:
        print('input not on the list')







def GroceryListMenu():
    print(f'Welcome to Grocery List')
    printfinalarray()
    print('Below are the options you can choose')
    print(f'1. Change Information \n 2. Delete Information \n 3. Return')
    choice = int(input('What would you like to do: '))

    match choice:
        case 1:
            changeInformation()
        case 2:
            print("2")
            deleteInformation()
        case 3:
            OptionsMenu()

    # if choice == 1:
    #     changeInformation()
    # elif choice == 2:
    #     deleteInformation()
    # elif choice == 3:
    #     OptionsMenu()
    # else:
    #     print(f'Choice was not within options')







def changeInformation():
    itemlookup = inputnumber() - 1
    name[itemlookup] = input(" Enter new name: ")
    productCode[itemlookup] = input("Enter new Product Code: ")
    quantity[itemlookup] = input("Enter new Quantity: ")
    price[itemlookup] = input("Enter new Price: ")


    GroceryListMenu()


def deleteInformation():
    itemlookup = inputnumber() - 1
    name[itemlookup] = '-x-'
    productCode[itemlookup] = 0
    quantity[itemlookup] = 0
    price[itemlookup] = 0
    GroceryListMenu()


def inputnumber():
    return int(input("Enter item to edit: "))


def printfinalarray():
    print(name)
    print(finalarray)

def Clearterminal():
    print("\033c", end="", flush=True)


# ----------------------------------------------------------------
# This section and anything that comes after is for AI Quiz 1
def Retry():
    print('Would')
def inputword():
    return input("Input your word: ")

def outputcombinedword():
    inputString = inputword()
    CombinedString = inputString + " * " + sampleString
    ParsedString = CombinedString[::-1]
    SinputString = inputString[1:-1]
    SsampleString = sampleString[1:-1]
    CombinedSstring = SinputString + " * " + SsampleString
    ParsedSstring = CombinedSstring[::-1]

    print(f' Input txt: {inputString} '
          f'\n Sample txt: {sampleString} '
          f'\n Combined txt: {CombinedString} '
          f'\n Parsed string:  {ParsedString} '
          f'\n Shortened Input string: {SinputString} '
          f'\n Shortened Sample string: {SsampleString} '
          f'\n Combined Shortened string: {CombinedSstring} '
          f'\n Parsed Shortened string: {ParsedSstring}')

    #number.isnumeric()
def greaterorlessthan():
    n1, n2 = input('Enter Number[1]: '), input('Enter Number[2]: ')
    if n1.isnumeric() and n2.isnumeric():
        n1, n2 = float(n1), float(n2)
        print(f'{n1}=={n2}'if n1 == n2
              else f'{n1}<={n2}'if n1 <= n2
                    else f'{n1}>={n2}'if n1 >= n2
                            else f'{n1} and {n2} is NOT between 0-10')
        print(f'{n1} and {n2} is between 0 and 10' if n1 and n2 <= 10 else f'{n1} and {n2} is not between 0 and 10')


    else:
        print('Invalid Input')





