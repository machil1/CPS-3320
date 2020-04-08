import bs4
from bs4 import BeautifulSoup
import requests

#Lawrence Machi III
#This program will ask a user for what HTML attribute they are looking for
#then ask the name of that attribute they are looking for, or if it is a
#script then it will print all of the scripts in the program. If it
#is a class or id and you input the name of that attribute, it will then
#print the source code that contains that fields.

#Function to pull HTML code data and then to look for a name of a div id and to
#print the source code associated with those cases search
def lookUpID(divID):
    #This function will look up a specific ID you are looking for 
    #Get the website data and store to variable
    req = requests.get('http://cyberhire.org')
    cont = req.content
    
    #Store information as HTML object using BeautifulSoup
    websiteData = bs4.BeautifulSoup(cont,"lxml")

    #To print the website data and look for anything else uncomment this line
    #print(websiteData)
    
    #Find the div class name that we are looking for
    divLookUp = websiteData.find_all(id = divID)
    
    #Print the HTML code
    if len(divLookUp) == 0:
        print("Nothing was found.")
    else:
        for i in divLookUp:
            print(i)

def lookUpScript():
    #This function will print the scripts that you put in the program 
    #Get the website data and store to variable
    req = requests.get('http://cyberhire.org')
    cont = req.content
    
    #Store information as HTML object using BeautifulSoup
    websiteData = bs4.BeautifulSoup(cont,"lxml")

    #To print the website data and look for anything else uncomment this line
    #print(websiteData)
    
    #Find the div class name that we are looking for
    divLookUp = websiteData.find_all("script")

    #Print the HTML code
    if len(divLookUp) == 0:
        print("Nothing was found.")
    else:
        for i in divLookUp:
            print(i)

#Function to pull HTML code data and then to look for a name of a div class and to
#print the source code associated with those cases search.
def lookUpClass(divClass):
    #This function will look up classes that you look for in the program
    #Get the website data and store to variable
    req = requests.get('http://cyberhire.org')
    cont = req.content
    #Store information as HTML object using BeautifulSoup
    websiteData = bs4.BeautifulSoup(cont,'lxml')

    #To print the website data and look for anything else uncomment this line
    #print(websiteData)
    
    #Find the div class name that we are looking for
    divLookUp = websiteData.find_all(class_ = divClass)
    
    #Print the HTML code
    if len(divLookUp) == 0:
        print("Nothing was found.")
    else:
        for i in divLookUp:
            print(i)

#The main function that will ask the user for a input to search for a
#div id or div class. Then if the right cases were correctly inputted.
#Then we will start one of the two programs depending on what the user inputted.
def main():
    print("This is my website I am currently working on.")
    print("This program will take a input from you to look for a HTML id, class, or script.")
    print("Then ask for the name of that attribute and print the source code.\n")
    
    print("Input 'class' and then one of the following examples: 'JobPosting','Search','Container','tab1','create','dropbutton1'\nto see the source code.")
    print("Search for scripts in the program inputting 'script'.")
    print("Input 'id' and then one of the following examples: 'mainform','logindiv','loginbtn','cancel' to see the source code.\n")

    #While loop to have the user input whether they want to look for a div id or div class
    #and check for cases if inputted the wrong attribute
    while True:
        IDorClass = input("Enter 'id' if you're looking for a ID, 'class' if you're looking for a class, lastly 'script' to print the scripts: ").lower()
        if(IDorClass == "id" or IDorClass == "class" or IDorClass == "script"):
            break
        else:
            print("Incorrect input, try again.")

    print("\nThis is case sensitive, so put the exact class/ID you are looking for\n")
    #If statements to check whether the user inputted id or class.
    #Then ask the user the name of the id or class they're looking for
    #then to take that and start the program.
    if(IDorClass == "id"):
        divID = input("Enter a id you are looking for:")
        lookUpID(divID)
    elif(IDorClass == "class"):
        divClass = input("Enter a class you want to look for:")
        lookUpClass(divClass)
    elif(IDorClass == "script"):
        lookUpScript()
main()
