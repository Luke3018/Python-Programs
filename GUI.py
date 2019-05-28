from tkinter import * #impor the GUI library

#function to open and store the league in a list 
def createLeague():
    myfile = open("premier.csv")
    
    myfile.readline()
    myfile.readline();
    league = []
    for line in myfile:
        line = line.split(',')
        points = int(line[2])*3 + int(line[3])
        line.append(points)
        league.append(line)
    return league

#function to calculate the total points of a given  team
def getPoints(name,league):
    for team in league:
        if name in team[0]:
            return(team[5])
    return -1 #returns -1 if teamis not part of list

#function to pass name and list to getPoints  and then store
def p():
    score.set(getPoints(name.get(), league))

#function to find the top team in the league
def highestScore(league):
    winner = league[0]
    for team in league:
        if team[5] > winner[5]:
            winner = team
        return (winner)

#function to pass league into highestScore and then store 
def t():
    top.set(highestScore(league))

#creates the graphical user interface
root = Tk()
root.title("Football")

#label for team and input textbox
Label(root, text="team").grid(row=0, column=0)
name=StringVar()
Entry(root, textvariable=name).grid(row=0, column=1)

#label points name tag
Label(root, text="points").grid(row=3, column=0)
score=IntVar()

#label to show team points(output)
Label(root, textvariable=score).grid(row=3, column=1)

#button to find given teams points
button = Button(root, text="Points", command=p)
button.grid(row=0, column=2, columnspan=2)

#button to find top team in league
b = Button(root, text="Top Team", command=t)
b.grid(row=2, column=0)

#label to output top team on
top=StringVar()
Label(root,textvariable=top).grid(row=2, column=1)

#buttom to close the grahics
Button(root, text="quit", command=root.destroy).grid(row=3, column=10)

league = createLeague()
root.mainloop()

