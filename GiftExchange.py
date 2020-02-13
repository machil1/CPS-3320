# Gift-assigner program
#Lawrence Machi III
import random

numPeople = int(input("How many people are playing? "))
givers = []
receivers = []
print("Please enter their names: ")

# Get all of the players' names and add them to the list
for i in range(numPeople):
    givers.append(input(""))
    
'''
Randomly assign gift givers to gift receivers. Check to make sure that
nobody is assigned themselves (which is no fun!), and that each person can
only give one gift and can only receive one gift (no repeats). Keep trying
(looping) until everyone is giving a gift to someone else.
'''

#Make a empty list to append the receivers to a empty list so they dont get
#picked again.
move = []

for j in range(numPeople):
    #Pick a random person to assign a gift to.
    receivers = random.sample(givers, numPeople)
    #Removing the duplicates of the lists but using sets because when you use
    #the difference tool in sets it will remove duplicates. Equal to the elements present in givers but not receivers
    check = list(set(givers) - set(receivers))
    #Have to use try and except to go through the list
    #since the check list is empty.
    try:
        check.remove(j)
    except:
        #Pass will finish this loop and go back to the beginning 
        pass
    #Append the recievers to a new list so that they dont get picked again
    move.append(recievers)
     
# Print results

print()
print("Gift Assignments...")
for k in range(numPeople):
    print(givers[k], "will buy a gift for", receivers[k])
print()
