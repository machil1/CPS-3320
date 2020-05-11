import winsound
from func_timeout import *
import datetime
from threading import Timer
import pandas as pd
from tkinter import *


#Lawrence Machi III
#This program will ask the user for a log entry at your selected time everyday,
#the computer must be awake and not asleep unless you use task schedualer on windows.
#Once the program initiates it will make a alarm sound and ask for a log and print it
#to the console show a visual log using tkinter and lastly append the logs into the text file.
#You will have a total of three times over a span of 30 seconds each being a total of 1 minute and
#30 seconds for testing purposes, if you dont it will raise an exception to try again tomorrow
#and exit the program!

#Displaying in dataframe
todayCol = datetime.date.today()

from datetime import datetime

today=datetime.today()
#This code below is when the code will run 
#Change day to today.day+1 and set your specific time so that it works every at that time
#Set day to today.day and replace the hour/minute/seconds to military time numbers to test program
EDIT=today.replace(day=today.day,hour=today.hour, minute=today.minute+1, second=0)
format_date=EDIT-today
finalTime=format_date.seconds+1

#This code will set the alarm 
duration = 1000
freq = 1000

#Ask the user to enter daily log
def quest():
    log = input("Enter your log for the day!\n")
    return log

#This code executes to ask the user at a max of 3 times
#Lastly to wait every 30 seconds and ask the user again.
def question():
    x=0
    log = ''
    while(x < 3):
        try:
            winsound.Beep(freq, duration)
            log = func_timeout(30,quest)
            if(len(log)>0):
                break
        except FunctionTimedOut:
            x+=1
    if x == 3:
        return log == None
    else: 
        return log

#This function will ask the user for a log entry calling the function
#Then if you were to repeat a log it will ask the user to ask again
#Once it is correct and not a repeat log, it will center the headings of the keys
#Then log the data and put it into a dataframe to format as a table and call the log func

def mainFunc():
    txt = open('Project3.txt','r')        
    try:
        while(True):
            log = question()
            data = {
                'Date' : [todayCol],
                'log':[log]
                }
            if log in txt.read():
                print("Try again")
            else:
                #Center the column header
                pd.set_option('colheader_justify', 'center')
                return False
    finally:
        if log == False:
            #If the user does not enter a log to exit the program
            raise Exception("You didn't input a log in time. Try again tomorrow!")
            exit()
        else:
            logEntry = pd.DataFrame(data)
            logData(logEntry)

#This function will first open the text file and append the dataframe the user entered
#to the text file. Then making sure we get rid of the indexes and since a dataframe is
#a different format we have to convert it to a string to append it to the file.
#Then using tkinter I made it so that it will show a visual aspect of the text logs,
#then also print your data to the console and lastly write it to the text file. Then,
#once you're all done, you can quit and end the program. 
def logData(logEntry):
        #Write log to text file
        insertTxt = open('Project3.txt','a')
        #Center the column header
        logEntry.style.set_properties(**{'text-align': 'center'})
        insertTxt.write(logEntry.to_string(index = False))
        insertTxt.write('\n\n')
        insertTxt.close()
        #Make a visual using tkinter
        root = Tk()
        Title = Label(root,text="Daily Journal!")
        Title.pack()
        showJournal = Text(root)
        showJournal.pack()
        root.title("Journal Entry")
        root.geometry("500x450+500+0")
        #This will read the file and write the contents of it to the console
        #and using tkinter to show a visual log of the contents
        printData = open('Project3.txt','r')
        data = printData.read()
        print (data)
        printData.close()
        #This closes the main window 
        showJournal.insert(END, data)
        Quit = Button(root, text="Quit", command=root.destroy)
        Quit.pack()
        root.mainloop()
        
def main():
    #This is used with to run the program everyday at the select time
    alarm = Timer(finalTime, mainFunc)
    alarm.start()    
main()

#Cant figure out how to delete prior user asking input
