from tkinter import *
import csv
root = Tk()

Names = []
entireSet = []
oppSelections = []
MagicPwr = 0
PhysicalPwr = 0

#Gets your CSV into lists
with open('champions.csv') as csvfile:
    championsCSV = csv.reader(csvfile, delimiter=',')
    for row in championsCSV:

        Names.append(row[0])
        entireSet.append(row)

#Calls your test print function
def printSelection1():
    global oppSelections
    global MagicPwr
    global PhysicalPwr

    selection = Opp1List.curselection()
    oppSelections.append(entireSet[selection[0]])
    Opp1LabelChose = Label(root, text="First oppenent is " + Names[selection[0]])
    Opp1LabelChose.grid(row=3, column=0)
    if entireSet[selection[0]][6] == "Physical":
        PhysicalPwr = PhysicalPwr + int(entireSet[selection[0]][1])
        print("Physical Power is: " + str(PhysicalPwr))
        print("Magic Power is: " + str(MagicPwr))

    elif entireSet[selection[0]][6] == "Magic":
        MagicPwr = MagicPwr + int(entireSet[selection[0]][1])
        print("Magic Power is: " + str(MagicPwr))
        print("Physical Power is: " + str(PhysicalPwr))

def printSelection2():
    global oppSelections
    global MagicPwr
    global PhysicalPwr

    selection = Opp2List.curselection()
    oppSelections.append(entireSet[selection[0]])
    Opp2LabelChose = Label(root, text="Second oppenent is " + Names[selection[0]])
    Opp2LabelChose.grid(row=3, column=1)
    if entireSet[selection[0]][6] == "Physical":
        PhysicalPwr = PhysicalPwr + int(entireSet[selection[0]][1])
        print("Physical Power is: " + str(PhysicalPwr))
        print("Magic Power is: " + str(MagicPwr))

    elif entireSet[selection[0]][6] == "Magic":
        MagicPwr = MagicPwr + int(entireSet[selection[0]][1])
        print("Physical Power is: " + str(PhysicalPwr))
        print("Magic Power is: " + str(MagicPwr))

def printSelection3():
    global oppSelections
    global MagicPwr
    global PhysicalPwr

    selection = Opp3List.curselection()
    oppSelections.append(entireSet[selection[0]])
    Opp3LabelChose = Label(root, text="Third oppenent is " + Names[selection[0]])
    Opp3LabelChose.grid(row=3, column=2)
    if entireSet[selection[0]][6] == "Physical":
        PhysicalPwr = PhysicalPwr + int(entireSet[selection[0]][1])
        print("Physical Power is: " + str(PhysicalPwr))
        print("Magic Power is: " + str(MagicPwr))

    elif entireSet[selection[0]][6] == "Magic":
        MagicPwr = MagicPwr + int(entireSet[selection[0]][1])
        print("Physical Power is: " + str(PhysicalPwr))
        print("Magic Power is: " + str(MagicPwr))

def printSelection4():
    global oppSelections
    global MagicPwr
    global PhysicalPwr

    selection = Opp4List.curselection()
    oppSelections.append(entireSet[selection[0]])
    Opp4LabelChose = Label(root, text="Fourth oppenent is " + Names[selection[0]])
    Opp4LabelChose.grid(row=3, column=3)
    if entireSet[selection[0]][6] == "Physical":
        PhysicalPwr = PhysicalPwr + int(entireSet[selection[0]][1])
        print("Physical Power is: " + str(PhysicalPwr))
        print("Magic Power is: " + str(MagicPwr))

    elif entireSet[selection[0]][6] == "Magic":
        MagicPwr = MagicPwr + int(entireSet[selection[0]][1])
        print("Physical Power is: " + str(PhysicalPwr))
        print("Magic Power is: " + str(MagicPwr))

def printSelection5():
    global oppSelections
    global MagicPwr
    global PhysicalPwr

    selection = Opp5List.curselection()
    oppSelections.append(entireSet[selection[0]])
    Opp5LabelChose = Label(root, text="Fifth oppenent is " + Names[selection[0]])
    Opp5LabelChose.grid(row=3, column=4)
    if entireSet[selection[0]][6] == "Physical":
        PhysicalPwr = PhysicalPwr + int(entireSet[selection[0]][1])
        print("Physical Power is: " + str(PhysicalPwr))
        print("Magic Power is: " + str(MagicPwr))

    elif entireSet[selection[0]][6] == "Magic":
        MagicPwr = MagicPwr + int(entireSet[selection[0]][1])
        print("Physical Power is: " + str(PhysicalPwr))
        print("Magic Power is: " + str(MagicPwr))


    if MagicPwr == 0:
        armorLabel = Label(root, text="The opposing team is 100% physical damage")
        armorLabel.grid(row=4, column=2)
    elif PhysicalPwr == 0:
        armorLabel = Label(root, text="The opposing team is 100% magic damage")
        armorLabel.grid(row=4, column=2)
    else:
        physArmorPerc = (PhysicalPwr/((MagicPwr + PhysicalPwr)*1.0))*100
        magArmorPerc = (MagicPwr/((MagicPwr + PhysicalPwr)*1.0))*100
        armorLabel = Label(root, text="The opposing team is %d magic damage and %d physical damage" % (magArmorPerc, physArmorPerc))
        armorLabel.grid(row=4, column=2)

#    print(physArmorPerc)
#    print(magArmorPerc)

#    armorLabel = Label(root, text="The opposing team is %d physical armor and %d magic armor." % (physArmorPerc, magArmorPerc))
#    armorLabel.grid(row=4, column=0)

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
for i in Names:

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
