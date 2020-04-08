import matplotlib.pyplot as Graph
import numpy as np
from pylab import *

#Lawrence Machi III
#This program will take data from a txt file which I made, and will populate
#the program, then for each county and their cases, I made it so that each one
#was put into a list. So that there is a string name and number of the cases,
#for each list(county) so it is set up as ['Bergen',2482].
#Then I had to set up the window, as for the position and placement, and populating
#the x-axis and y-axis, making sure it is a bar graph and lastly setting up the
#labels and title.

#This places the graph in a specific position and size.
graphPlacement = get_current_fig_manager()
graphPlacement.window.wm_geometry("800x800+500+0")

#Opening the text file which has the county and number of cases
#and stripping the \n from the file.
new = open("COVID-19 NJ.txt","r")
NJ = new.read()
lines = NJ.split("\n")
temp = []

#Splitting the spaces and closing the file
for i in lines:
    temp.append(i.split(" "))
new.close()

#Assigning each county and there amount of cases to a list
#Making it as ['Bergen',2482] and the printing the amount of cases for
#each county to the console.
for j in temp:
    if "Bergen" in j:
        Bergen = j
        print("Bergen has",Bergen[1],"cases")
    if "Essex" in j:
        Essex = j
        print("Essex has",Essex[1],"cases")
    if "Hudson" in j:
        Hudson = j
        print("Hudson has",Hudson[1],"cases")
    if "Union" in j:
        Union = j
        print("Union has",Union[1],"cases")
    if "Middlesex" in j:
        Middlesex = j
        print("Middlesex has",Middlesex[1],"cases")
    if "Passaic" in j:
        Passaic = j
        print("Passaic has",Passaic[1],"cases")
    if "Monmouth" in j:
        Monmouth = j
        print("Monmouth has",Monmouth[1],"cases")
    if "Ocean" in j:
        Ocean = j
        print("Ocean has",Ocean[1],"cases")
    if "Morris" in j:
        Morris = j
        print("Morris has",Morris[1],"cases")
    if "Somerset" in j:
        Somerset = j
        print("Somerset has",Somerset[1],"cases")
    if "Mercer" in j:
        Mercer = j
        print("Mercer has",Mercer[1],"cases")
    if "Camden" in j:
        Camden = j
        print("Camden has",Camden[1],"cases")
    if "Burlington" in j:
        Burlington = j
        print("Burlington has",Burlington[1],"cases")
    if "Sussex" in j:
        Sussex = j
        print("Sussex has",Sussex[1],"cases")
    if "Gloucester" in j:
        Gloucester = j
        print("Morris has",Gloucester[1],"cases")
    if "Hunterdon" in j:
        Hunterdon = j
        print("Hunterdon has",Hunterdon[1],"cases")
    if "Warren" in j:
        Warren = j
        print("Warren has",Warren[1],"cases")
    if "Atlantic" in j:
        Atlantic = j
        print("Atlantic has",Atlantic[1],"cases")
    if "Cumberland" in j:
        Cumberland = j
        print("Cumberland has",Cumberland[1],"cases")
    if "CapeMay" in j:
        Capemay = j
        print("Cape May has",Capemay[1],"cases")
    if "Salem" in j:
        Salem = j
        print("Salem has",Salem[1],"cases")

#X-axis counties, assigning the names of each county to each bar
counties = [Bergen[0],Essex[0],Hudson[0],Union[0],Middlesex[0],Passaic[0],Monmouth[0],Ocean[0],
            Morris[0],Somerset[0],Mercer[0],Camden[0],Burlington[0],Sussex[0],Gloucester[0],Hunterdon[0],
            Warren[0],Atlantic[0],Cumberland[0],Capemay[0],Salem[0]]
#Y-axis county cases assigning this to each bar to populate the bar and y-axis
numbers = [Bergen[1],Essex[1],Hudson[1],Union[1],Middlesex[1],Passaic[1],Monmouth[1],Ocean[1],
           Morris[1],Somerset[1],Mercer[1],Camden[1],Burlington[1],Sussex[1],Gloucester[1],Hunterdon[1],
           Warren[1],Atlantic[1],Cumberland[1],Capemay[1],Salem[1]]

#Below converts the string of numbers into numbers so we can use it in the
#matplotlib chart as integers using casting
numberlist = []
for i in numbers:
    numberlist.append(int(i))

#The amount of counties on the y-axis
y = np.arange(len(counties))

#Making the graph a bar graph and populating the numbers of each county
#with the using y as the total number of counties.
Graph.bar(y,numberlist, align = 'center')
#The names of each county and populating the x-axis with all the names of the
#counties and make their names vertial since the naes are long
Graph.xticks(y,counties,rotation = "vertical")
#This is what pushed the graph up toward the top of the window
Graph.tight_layout()
#This will plot the graph
Graph.plot()

#Setting up the bar graph as for the title,the axis for x and y
#then being able to save the graph and show it.
Graph.xlabel('Counties')
Graph.ylabel('Cases')
Graph.title('COVID-19 Stats in New Jersey as of March 30 2020')
Graph.savefig("COVID-19.png")
Graph.show()
