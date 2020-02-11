#Lawrence Machi III
#Make a scrabble game using if statements and functions

#Use if statements to check for a letter inputted by user and return a score
def letterScore(letter):
    if letter in ' a n o e r s t u i l ':
        return 1
    if letter in ' d g ':
        return 2
    if letter in ' b c m p ':
        return 3
    if letter in ' f h v w ':
        return 4
    if letter in ' k ':
        return 5
    if letter in ' j x ':
        return 8
    if letter in ' q z ':
        return 10
    else:
        return 0

#Using the letterScore function traverse through the word inputted by user
#and check each letter and return a score for the entire word
def wordScore(word):
    score = 0
    for current in word:
        score += letterScore(current)
    return score

#Implemented a total score
def main():
    totalScore = 0
    letter = input("Enter a letter ").lower()
    print("Your score is:" , letterScore(letter))
    while True:
        #Use .lower() to compensate for any case characters
        word = input("Enter a word ").lower()
        print("Your score is:" ,wordScore(word))
        #Below add the total score 
        totalScore += wordScore(word)
        #Use continue to keep playing the game and accumulate a total score
        userInp = input("If you want to continue type yes if not type no.").lower()
        if(userInp == "yes"):
            continue
        elif(userInp == "no"):
            print("Your total score is:", totalScore)
            return False
        else:
            return False
main()
