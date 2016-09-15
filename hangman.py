'''
@author: Abhinav Kurada
@date: 9/15/16

Program Description:

User guesses a secret word that the programmer has selected.
They guess it letter by letter. If they guess the right letter,
that letter is revealed in the word.
If they guess it wrong they get a strike. If they get 5 strikes they lose. 
'''

username = input("Hey, what is your name: ")


#Pick the Secret Word and then add each letter to a seperate element in the list
secretWord = "Jumpman"

wordArray = []
wordChecker =[]

for letter in secretWord:
    wordArray.append(letter)
    wordChecker.append(0)


errorCount = 0;
status = False

#if wordCheckValue == len(secretWord) --> status ==True
wordCheckValue =0


#Repeat Guessing Method Below

def repeatGuess(userGuess, status, errorCount):
    thisLoopUp =0
    if status == True:
        print("Congratulations: You have won the Hangman game.")
        print("The Secret Word was: " + secretWord)
    elif any((c in userGuess) for c in wordArray): # if letter is in word
        wordCheckValue = 0
 
             
        for index, letter in enumerate(wordArray):
            if userGuess == letter:
                if (wordChecker[index] != 1):
                    wordChecker[index] =1
                    thisLoopUp+=1
                else:
                    print("You already guessed that letter")

        #traverse through wordChecker -- if the whole thing is 1's then status == True

        
        for index in range(len(secretWord)):
            if (wordChecker[index] == 1):
                wordCheckValue+=1

        if (thisLoopUp > 0): 
            print("Nice. You just guessed " + str((thisLoopUp)) + " of the letters remaining")
        print("There are " + str(len(secretWord) - wordCheckValue) + " letters left in the secret word")
        
        if (len(secretWord) - wordCheckValue) == 0 :
            status = True
  
        else:
            userGuess = input("Guess again: ")
        
        repeatGuess(userGuess, status, errorCount)

         
        # if letter is not in the word
    else:
        errorCount+=1
        if errorCount >= 5:
            print("You lose!")
            print("The Secret Word was: " + secretWord)
        else:
            userGuess = input("Sorry bro. Guess again: ")
            repeatGuess(userGuess, status, errorCount)

        
#Repeat Guessing Method Above
        
userGuess = input("Hey " + username + ". Let's Play Hangman! Guess a letter: ")
repeatGuess(userGuess, status, errorCount)
    


