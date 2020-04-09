from tkinter import *
import random

#Lawrence Machi III
#This is a Rock Paper Scissors game using tkinter! There are store functions in
#the top of the program which will store the string value and start the game
#so that the program could compare values in the various if statements. Then
#there is a popup function that will show when either the user or computer
#reaches a score of three, and will stay up for a few seconds and then
#print to the console the score! Then toward the bottom of the program, it is
#setting up the window, the placement, size, and the button widgets, which are
#repeated in the game function!

#Store the string names rock, paper, scissor into variables and then play game
def storeRock():
    rock = "rock"
    game(rock)
def storePaper():
    paper = "paper"
    game(paper)
def storeScissors():
    scissors = "scissors"
    game(scissors)

#Make a game over pop up window using a label widget
def popup(gameOver):
    #Setting up the label for game over
    popup = Tk()
    popup.title("Game Over")
    game = Label(popup, text=gameOver)
    game.pack(fill= "none",expand = True,pady = 5)
    print(gameOver)
    popup.after(10000,popup.destroy)
    
def game(user):
    #Setting up the window for when the user presses rock, paper, scissors
    #the game will make a text box showing who wins and the current score
    T = Text(master = root,height = 4, width = 25)
    T.pack(expand=True, fill=BOTH)

    #Assign a random pick to the computer
    choice = "rock","paper","scissors"
    computer = random.choice(choice)
    
    #Using a global variable since we need to keep hold of the user and computer score when pressing a button
    global userscore
    global computerscore
    
    cpuWin = "Computer Wins!\n"
    userWin = "User Wins!\n"
    tie = "Same Pick!\n"

    #If statements for the actual game, checking cases when the user presses rock paper or scissors
    #Then it will insert a text box with the user and computers score and who wins
    if(user == computer):
        #This code which is used in every if statement, will add color to the
        #background, to show for who wins, and insert the to the window
        T.tag_config('tie',background = 'yellow')
        T.insert(END,tie,'tie')
    if(user == "rock"):
        if(computer == "scissors"):
            userscore+=1
            T.tag_config('user',background = 'green')
            T.insert(INSERT,userWin,'user')
        elif(computer == "paper"):
            computerscore+=1
            T.tag_config('computer',background = 'red')
            T.insert(INSERT,cpuWin,'computer')
    elif(user == "paper"):
        if(computer == "scissors"):
            computerscore+=1
            T.tag_config('computer',background = 'red')
            T.insert(INSERT,cpuWin,'computer')
        elif(computer == "rock"):
            userscore+=1
            T.tag_config('user',background = 'green')
            T.insert(INSERT,userWin,'user')
    elif(user == "scissors"):
        if(computer == "rock"):
            computerscore+=1
            T.tag_config('computer',background = 'red')
            T.insert(INSERT,cpuWin,'computer')
        elif(computer == "paper"):
            userscore += 1
            T.tag_config('user',background = 'green')
            T.insert(INSERT,userWin,'user')

    #If statements for when the user or computer wins to print and start the popup
    #message then destory the window of the game after three seconds, or to
    #continue the game and insert the score
    if(userscore == 3):
        #These statements will make a message and convert a int to a string so we can
        #concatenate and make a score message and end message if the user or computer wins,
        #and call the popup which will print game over, if we go to else, it will continue the game.
        answer = "Your score: " + str(userscore) + "\nComputer Score: " + str(computerscore)
        T.insert(INSERT,answer)
        endMessage = "Congrats! The user won, with a total score of: " + str(userscore) + " and the computer had: " + str(computerscore)
        popup(endMessage)
        root.after(3000,root.destroy)
    elif(computerscore == 3):
        answer = "Your score: " + str(userscore) + "\nComputer Score: " + str(computerscore)
        T.insert(INSERT,answer)
        endMessage = "NOO! The computer won, with a total score of: " + str(computerscore) + " and the user had: " + str(userscore)
        popup(endMessage)
        root.after(3000,root.destroy)
    else:
        answer = "Your score: " + str(userscore) + "\nComputer Score: " + str(computerscore)
        T.insert(INSERT,answer)

#Setting up the main window and parameters for size and where to position it
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("500x800+500+0") 

#Setting up labels for explaining the game
lbl = Label(root,text="You will be playing against a computer! Who ever gets to three first wins!")
lbl.pack()
lbl1 = Label(root,text = "Click one of the buttons to play!")
lbl1.pack()

#Making the buttons for rock
rockButton = Button(root,text = "Rock", command = storeRock)
rockButton.pack(side = TOP)

#Making the buttons for paper
paperButton = Button(root,text = "Paper",command = storePaper)
paperButton.pack(side = TOP)

#Making the buttons for scissors
scissorsButton = Button(root,text = "Scissors",command = storeScissors)
scissorsButton.pack(side = TOP)

#Declare the score variables for the user and computer when the user
#presses a button
userscore = 0
computerscore = 0

#To continue the game 
root.mainloop()
