import random

username = input("Hey, what is your name: ")

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber,maxNumber)

message ="Hey {2}, I am thinking of a number between {0} and {1}."
print(message.format(minNumber, maxNumber, username))

print(magicNumber)
prompter =("Guess my number: ")
userGuess = int(input(prompter))
count =0;

outputString = "Awesome {0}, You guessed the magic number correct in {1} tries"

status = False

#Function of all the stuff below this that has inputs of userGuess, status, count



def repeatGuess(userGuess, status, count):


    if (status):
            print(outputString.format(username, count))
            return None
        
    else: 
        if userGuess > magicNumber: 

            highP = "Guess lower: "
            userGuess = int(input(highP))
            count+=1
            repeatGuess(userGuess, status, count)
            return None

        elif userGuess < magicNumber:

            lowP = "Guess higher: "
            userGuess = int(input(lowP))
            count+=1
            repeatGuess(userGuess, status, count)
            return None
            
        else:
            status = True
            count+=1
            repeatGuess(userGuess, status, count)
            return None
        

repeatGuess(userGuess, status, count)

      


