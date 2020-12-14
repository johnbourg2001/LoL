from tkinter import *
import csv
root = Tk()

list = []

with open('champions.csv') as csvfile:
    championsCSV = csv.reader(csvfile, delimiter=',')
    for row in championsCSV:

        list.append(row[0])

myList = Listbox(root, selectmode = SINGLE)

def printSelection():
    selection = myList.curselection()
    print(selection[0])


myButton = Button(root, text = "Champion Selection", command = printSelection)

j = 0

for i in list:

    myList.insert(j, i)
    j = j + 1



myList.grid(row=0, column=0)
myButton.grid(row=3, column=0)


root.mainloop()
