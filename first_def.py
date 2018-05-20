numToCheck = input("Enter a number to check: ")
answer = checkIfPrime(numToCheck)
if answer == True:
    print("Prime!")

def checkIfPrime (numToCheck):a
    for x in range(2, numToCheck):
        if (numToCheck%x == 0):
            return False
        return True