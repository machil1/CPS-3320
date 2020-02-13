#Lawrence Machi III

#Below will pick a random word to choose for hangman
import random
A = ['p','y','t','h','o','n']
B = ['d','o','m','a','n','s','k','i']
C = ['k','e','a','n']
D = ['p','o','d','c','a','s','t']
selection = [A,B,C,D]
selection = random.choice(selection)


#Once the word is picked we will generate the dash marks for number of
#letters in the word
L = ['_'] * len(selection)

play = True
wrongAns=['_','_','_','_','_','_']
wrong = 0
j = 0
while play == True:
    # Ask the user to guess a letter
    # Check to see if that letter is in the Answer

    i = 0
    letter = str(input("Guess a letter: ")).lower()
    for currentletter in selection:
        #Check if the letter is not the current letter if not go to next letter
        #to traverse through the word
        if letter != currentletter:
            pass
        # If the letter the user guessed is found in the answer,
        # set the underscore in the user's answer to that letter
        elif letter == currentletter:
            L[i] = letter
            pass
        #Check for letters that are not in the word, if it is not then
        #increase the amount of wrong tries and increment the index 
        if letter not in selection:
           wrong += 1
           wrongAns[j] = "x"
           j += 1
           print("Bad guess!")
           #The if statement will check if the amount of wrong guesses and
           #index is at six and if so it will end the game making it false
           #and break so we dont get a index out of bounds exception
           if(wrong == 6 and j == 6):
                print("Game over!")
                play = False
                break
           #The else statement will tell you how many wrong guesses you have
           #and then break from the initial for statement to ask for a new letter
           else:
               print("You currently have:",wrong, "wrong.")
               break
        i += 1
    # Display what the player has thus far (L) with a space
    # separating each letter
    print(' '.join(str(n) for n in L))
    print()
    print(wrongAns)
    print()
    # Test to see if the word has been successfully completed,
    # and if so, end the loop
    if selection == L:
        play = False
        print("GREAT JOB!")
        break
print("The word was:", selection)

