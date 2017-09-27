import hangmat
import time



def check():
    if counter == 1:
        hangmat.een()
    elif counter == 2:
        hangmat.twee()
    elif counter == 3:
        hangmat.drie()
    elif counter == 4:
        hangmat.vier()
    elif counter == 5:
        hangmat.vijf()
    elif counter == 6:
        hangmat.zes()




woord = "bilal"
counter = 0
gebruikte_letters = ""


while True:
    letter = input("type een letter ")
    print("deze letters heb je gebruikt: " + gebruikte_letters)
    if letter == "?":
         raad = input("probeer het woord te raden dan: ")
         if raad == woord:
             print("je hebt het woord geraden")
             break
         else:
             print("test")
             counter += 1
             check()
