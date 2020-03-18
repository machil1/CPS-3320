import random
#Lawrence Machi III
#This is a mutual friends program randomizing peoples names and assigning them to too each person out of
#the eight names, then the user can pick two names and compare them, if they have one or more friends in
#common they will be returned the number of friends in common and who they are. If there is no friends in
#common it will show there arent any friends. We then can continue playing after until the user decides to
#the program.

#This function will randomize the friends and randomly assign 4 friends to each person, at first making seperate lists
#then putting them all to one list and assigning a string name to each 4 friends
def randomize():
    #numPeople = 8
    friendsNum = ["jack","max","will","mario",
                  "wilma","shannon","elaine",
                  "jordan","austin","sean",
                  "adam","andrea","deedee",
                  "patricia","marleen","sarah",
                  "neil","dishant","ronak","kathy"]
    
    #Assign the random 4 friends to the people
    #Using a for loop pick 2 names 
    for i in range(3):
        Lawrence = random.sample(friendsNum,4)
        Mark = random.sample(friendsNum,4)
        Matt = random.sample(friendsNum,4)
        John = random.sample(friendsNum,4)
        Silvia = random.sample(friendsNum,4)
        Shayla = random.sample(friendsNum,4)
        Christina = random.sample(friendsNum,4)
        Mary = random.sample(friendsNum,4)

    #Assign a name to each list to know which person has which set of friends 
    newList = [("lawrence",Lawrence),
               ("mark",Mark),
               ("matt",Matt),
               ("john",John),
               ("silvia",Silvia),
               ("shayla",Shayla),
               ("christina",Christina),
               ("mary",Mary)]
    return newList

def friend1(name1,name2,newList):
    #Temporary storage
    temp = []
    temp1 = []

    #Used to store the mutual friends
    commonFriends = []
    #Used to see how many friends each person has
    friendCount = 0

    #Using the inputs the user gives, find the names in the list and take their friends to a temporary storage
    for i in newList:
        if name1 == i[0]:
            temp = i[1]
        if name2 == i[0]:
            temp1 = i[1]
            
    #Once taken to temp storage traverse thorough them and find the mutual friends between the two people
    #If found then append that friend name to a list where it only displays the mutual friends
    for common in temp:
        if common in temp1:
            commonFriends.append(common)

    #This if else statement prints the amount of mutual friends from 0 to how many friends we find as mutual    
    if commonFriends == []:
        return "They have 0 friends in common!"
    elif len(commonFriends) >= 1:
        friendCount+=len(commonFriends)
        print("They have",friendCount,"in common!")
        return "The mutual friends they have in common is",commonFriends
          
def main():
    while(True):
        print("Welcome to my recommended friends program!")
        #randomize the names 
        newList = randomize()
        #Make a temp list so that we can make a error catching loop to check 
        fakelist = []
        for i in newList:
            print(i[0])
            
            #This commented code below will print the name and friends assigned to that person.
            #Just comment the above print statement
            #print(i[0],i[1])
            
            fakelist.append(i[0])

        #Error catching loop if the name is not in the list to print a error
        #Then if both names are in the list if it is to break from the loop 
        while(True):
            name1 = input("Enter a name from the list. ").lower()
            name2 = input("Enter a another name from the list. ").lower()
            if name1 not in fakelist:
                print("Error:", name1,"not in list.")
            if name2 not in fakelist:
                print("Error:", name2,"not in list")    
            if name1 not in fakelist and name2 not in fakelist:
                print("Error: Both names are not in the list please try again.")
                print()
            if name1 == name2:
                print("Error cannot input the same name.")
            elif name1 in fakelist and name2 in fakelist:
                break
            
        #Run the program     
        print("Lets see if they have mutual friends...")
        print(friend1(name1,name2,newList))
        
        #Implemented a option to continue playing the game
        playAgain = input("Would you like to try again? Input Yes or No!").lower()
        if(playAgain == "yes"):
            print()
            continue
        elif(playAgain == "no"):
            print("Thanks for playing!")
            break
        else:
            break
        print()
main()   
