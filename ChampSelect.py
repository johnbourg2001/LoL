from tkinter import *
import csv
root = Tk()

list = []
entireSet = []

#Gets your CSV into lists
with open('champions.csv') as csvfile:
    championsCSV = csv.reader(csvfile, delimiter=',')
    for row in championsCSV:

        list.append(row[0])
        entireSet.append(row)

#Calls your test print function
def printSelection1():
    selection = Opp1List.curselection()
    print(entireSet[selection[0]])

def printSelection2():
    selection = Opp2List.curselection()
    print(entireSet[selection[0]])

def printSelection3():
    selection = Opp3List.curselection()
    print(entireSet[selection[0]])

def printSelection4():
    selection = Opp4List.curselection()
    print(entireSet[selection[0]])

def printSelection5():
    selection = Opp5List.curselection()
    print(entireSet[selection[0]])

#All of your Opp Label initializaiton
Opp1Label = Label(root, text="1st Opponent Champion")
Opp2Label = Label(root, text="2nd Opponent Champion")
Opp3Label = Label(root, text="3rd Opponent Champion")
Opp4Label = Label(root, text="4th Opponent Champion")
Opp5Label = Label(root, text="5th Opponent Champion")

#All of your Opp Button initializaiton
Opp1Button = Button(root, text = "Opposing Champion Selection", command = printSelection1)
Opp2Button = Button(root, text = "Opposing Champion Selection", command = printSelection2)
Opp3Button = Button(root, text = "Opposing Champion Selection", command = printSelection3)
Opp4Button = Button(root, text = "Opposing Champion Selection", command = printSelection4)
Opp5Button = Button(root, text = "Opposing Champion Selection", command = printSelection5)


#All of your list initializaiton
Opp1List = Listbox(root, selectmode = SINGLE)
Opp2List = Listbox(root, selectmode = SINGLE)
Opp3List = Listbox(root, selectmode = SINGLE)
Opp4List = Listbox(root, selectmode = SINGLE)
Opp5List = Listbox(root, selectmode = SINGLE)

j = 0
for i in list:

    Opp1List.insert(j, i)
    Opp2List.insert(j, i)
    Opp3List.insert(j, i)
    Opp4List.insert(j, i)
    Opp5List.insert(j, i)
    j = j + 1



#Grid placement
Opp1List.grid(row=1, column=0)
Opp2List.grid(row=1, column=1)
Opp3List.grid(row=1, column=2)
Opp4List.grid(row=1, column=3)
Opp5List.grid(row=1, column=4)

Opp1Label.grid(row=0, column=0)
Opp2Label.grid(row=0, column=1)
Opp3Label.grid(row=0, column=2)
Opp4Label.grid(row=0, column=3)
Opp5Label.grid(row=0, column=4)

Opp1Button.grid(row=2, column=0)
Opp2Button.grid(row=2, column=1)
Opp3Button.grid(row=2, column=2)
Opp4Button.grid(row=2, column=3)
Opp5Button.grid(row=2, column=4)

root.mainloop()
