# let's get their name.
#serName = input("What is your name, loser? ")
# now that we have their name, let's do some stuff
#rint("Disappointed to meet you, ", userName)
# now for their age
#serAge = input("How many orbits around the sun are you, " + userName + "?")
#rint("you old fuck, you're " + userAge + " years old!")
#count the length of the name
#rint("The length of that name is ",len(userName))

# now for some flow
userCount = 0

while userCount < 5:
    userName = input("What is your name, loser? ")
    print("Disappointed to meet you, ", userName)
    if userName == "Bob":
        print("Nice face, Bob")
        userCount = userCount + 1

    elif userName == "Alice":
        print("Nicer face, Alice")
        userCount = userCount + 1

    else:
        print("What are nose?")
        userCount = userCount + 1

