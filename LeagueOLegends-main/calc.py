from tkinter import *
import csv
root = Tk()

with open('champions.csv') as csvfile:
    championsCSV = csv.reader(csvfile, delimiter=',')
    for row in championsCSV:
        print (row)

list = ("Morgana", "Perl", "one", "Two", "Three")

myLabel = Label(root, text = "Hello World!")
myLabel.pack()
myList = Listbox(root)

j = 0

for i in list:

    myList.insert(j, i)
    j = j + 1

myList.pack()

root.mainloop()
