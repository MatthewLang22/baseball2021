# Matthew Lang and Alex Heffner
# 11-24-2021
# CS 4620 Final Project

import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import *

LARGE_FONT= ("Verdana", 12)

connection = sqlite3.connect("baseball.db")
cursor = connection.cursor()


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def execute_queries(connection, queries):
    cursor = connection.cursor()
    try:
        cursor.executescript(queries)
        connection.commit()
        print("Queries executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def hitting_query():
    print("Players who hit above .300 and had over 200 At-Bats:")
    testing = cursor.execute("SELECT FNAME, LNAME, AVG FROM Batting where AVG > .300 AND AB > 200").fetchall()
    print(testing)

def pitching_query():
    print("Pitchers who had above 200 strikeouts:")
    testing = cursor.execute("SELECT FNAME, LNAME, SO from Pitching where SO > 200").fetchall()
    print(testing)

def fielding_query():
    print("Fielders with a defensive war above 2: ")
    testing = cursor.execute("SELECT FNAME, LNAME FROM Fielding where DWAR > 2").fetchall()
    print(testing)

def pirates_query():
    print("Pirates 40 man roster: ")
    testing = cursor.execute("SELECT FNAME, LNAME FROM Pirates").fetchall()
    print(testing)

def select_all(checkBoxs, checkBoxsOG):
    for num in range(len(checkBoxs)):
        checkBoxs[num].select()
    for num in range(len(checkBoxsOG)):
        checkBoxsOG[num].select()
def deselect_all(checkBoxs, checkBoxsOG):
    for num in range(len(checkBoxs)):
        checkBoxs[num].deselect()
    for num in range(len(checkBoxsOG)):
        checkBoxsOG[num].deselect()

def clear_batting_pitching_fielding(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, checkBoxs, checkBoxsOG):
    fname_input.delete('1.0', END)
    lname_input.delete('1.0', END)
    position_variable.set("") # default value
    position_options = OptionMenu(self, position_variable, "", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
    team_variable.set("")
    team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
    for num in range(12):
        checkBoxs[num].deselect()
    for num in range(len(lablesVariables)):
        lablesVariables[num].set("")
        gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
        lablesOptions[num]= gp_options
        lableInput[num].delete('1.0', END)
    for num in range(len(lablesVariables)+2):
        checkBoxsOG[num].deselect()
def batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name, lables, checkBoxsAnswOG, checkBoxsAnsw):
    querey = "SELECT FNAME, LNAME"
    if checkBoxsAnswOG[0].get() == 1:
        querey += ", POSITION"
    if checkBoxsAnswOG[1].get() == 1:
        querey += ", teams.TEAM"
    for num in range(len(checkBoxsAnswOG) - 2):
        if(checkBoxsAnswOG[num + 2].get() == 1):
            querey += ", " + lables[num].cget('text')
    table2name = ["CITY", "NICKNAME", "LEAGUE", "DIV", "GM","MANAGER", "STADIUM", "CAPACITY","SYEAR", "ADDRESS","PHONE", "WEBSITE"]
    for num in range(12):
        if(checkBoxsAnsw[num].get() == 1):
            querey += ", " + table2name[num]
    count = 0
    querey += " from " + name  + " INNER JOIN teams ON (" + name + ".TEAM = teams.TEAM)"
    if(fname_input.get("1.0",'end-1c') != ""):
        querey += (" where FNAME = " + "\'" + fname_input.get("1.0",'end-1c') + "\'")
        count += 1
    if(lname_input.get("1.0",'end-1c') != ""):
        if(count != 0):
            querey += " AND LNAME = "
            querey += ("\'" +lname_input.get("1.0",'end-1c') + "\'")
        else:
            count += 1
            querey += (" where LNAME = " + "\'" + lname_input.get("1.0",'end-1c') + "\'")
    if position_variable.get() != "":
        if(count != 0) :
            querey += " AND POSITION = " + "\'" + position_variable.get() +"\'"
        else:
            querey += " where POSITION = " + "\'" + position_variable.get() +"\' "
            count += 1
    if team_variable.get() != "":
        if(count != 0) :
            querey += " AND teams.TEAM = " + "\'" + team_variable.get() +"\'"
        else:
            querey += " where teams.TEAM = " + "\'" + team_variable.get() +"\'"
            count += 1
    for num in range(len(lables)):
        if lablesVariables[num].get() != "":
            if count != 0:
                querey += " AND " + lables[num].cget('text') + " " + lablesVariables[num].get() + " \'" + lableInput[num].get("1.0",'end-1c') + "\'"
            else:
                count +=1
                querey += " where " + lables[num].cget('text') + " " + lablesVariables[num].get() + " \'" + lableInput[num].get("1.0",'end-1c') + "\'"

    print("Querey: " , querey)

    users = execute_read_query(connection,querey)

    for user in users:
        print(user) 
    
class Baseball(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageBatting, PagePitching, PageFielding, PagePirates):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
      

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        batting_pic = PhotoImage(file = r"./images/battingpic.png")
        label = Label(image=batting_pic)
        label.image = batting_pic # keep a reference!

        pitching_pic = PhotoImage(file = r"./images/pitchingpic.png")
        label = Label(image=pitching_pic)
        label.image = pitching_pic # keep a reference!

        fielding_pic = PhotoImage(file = r"./images/fieldingpic.png")
        label = Label(image=fielding_pic)
        label.image = fielding_pic # keep a reference!

        pirates_pic = PhotoImage(file = r"./images/piratespic.png")
        label = Label(image=pirates_pic)
        label.image = pirates_pic # keep a reference!

        exit_pic = PhotoImage(file = r"./images/exitpic.png")
        label = Label(image=exit_pic)
        label.image = exit_pic # keep a reference!

        label1 = tk.Label(self, text = "CS 4620 Final Project")
        label1.config(font =("Courier", 50))
        label1.pack()

        l2 = tk.Label(self, text = "By: Matthew Lang and Alex Heffner")
        l2.config(font =("Courier", 30))
        l2.pack()

        blank1 = tk.Label(self, text = "")
        blank1.config(font =("Courier", 30))
        blank1.pack()

        Button(self, text = 'Click Me !', image = batting_pic, command=lambda:[controller.show_frame(PageBatting)]).pack()

        blank1 = tk.Label(self, text = "")
        blank1.config(font =("Courier", 30))
        blank1.pack()

        Button(self, text = 'Click Me !', image = pitching_pic, command=lambda:[controller.show_frame(PagePitching)]).pack()

        blank1 = tk.Label(self, text = "")
        blank1.config(font =("Courier", 30))
        blank1.pack()

        Button(self, text = 'Click Me !', image = fielding_pic, command=lambda:[controller.show_frame(PageFielding)]).pack()

        blank1 = tk.Label(self, text = "")
        blank1.config(font =("Courier", 30))
        blank1.pack()

        Button(self, text = 'Click Me !', image = pirates_pic, command=lambda:[controller.show_frame(PagePirates)]).pack()

        blank1 = tk.Label(self, text = "")
        blank1.config(font =("Courier", 30))
        blank1.pack()

        Button(self, text = 'Click Me !', image = exit_pic, command =lambda:[quit()]).pack()


class PageBatting(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Batting Filters", font=("Courier", 30))
        label.place(x = 200, y = 0)    
        name = "batting"

        fname_label = tk.Label(self, text="First name: ", font=("Courier", 18))
        fname_label.place(x = 35, y = 55)

        fname_input = Text(self, height = 1, width = 30)
        fname_input.place(x = 160, y = 60)

        lname_label = tk.Label(self, text="Last name: ", font=("Courier", 18))
        lname_label.place(x = 35, y = 85)

        lname_input = Text(self, height = 1, width = 30)
        lname_input.place(x = 160, y = 90)

        position_label = tk.Label(self, text="Position: ", font=("Courier", 18))
        position_label.place(x = 35, y = 115)

        position_variable = StringVar(self)
        position_variable.set("") # default value
        position_options = OptionMenu(self, position_variable, "", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
        position_options.place(x = 160, y = 120)

        team_label = tk.Label(self, text="Team: ", font=("Courier", 18))
        team_label.place(x = 35, y = 145)

        team_variable = StringVar(self)
        team_variable.set("") # default value
        team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
        team_options.place(x = 160, y = 150)

        lables = [] 
        checkBoxsOG = []
        checkBoxs = []
        lablesVariables = [] 
        lablesOptions = []
        lableInput = []

        lables.append(tk.Label(self, text="GP", font=("Courier", 18)))
        lables.append(tk.Label(self, text="AVG", font=("Courier", 18)))
        lables.append(tk.Label(self, text="AB", font=("Courier", 18)))
        lables.append(tk.Label(self, text="R", font=("Courier", 18)))
        lables.append(tk.Label(self, text="H", font=("Courier", 18)))
        lables.append(tk.Label(self, text="DOU", font=("Courier", 18)))
        lables.append(tk.Label(self, text="TRIP", font=("Courier", 18)))
        lables.append(tk.Label(self, text="HR", font=("Courier", 18)))
        lables.append(tk.Label(self, text="RBI", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SB", font=("Courier", 18)))
        lables.append(tk.Label(self, text="CS", font=("Courier", 18)))
        lables.append(tk.Label(self, text="BB", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SO", font=("Courier", 18)))
        lables.append(tk.Label(self, text="OBP", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SLG", font=("Courier", 18)))
        lables.append(tk.Label(self, text="OPS", font=("Courier", 18)))

        # Checkboxes
        checkBoxsAnswOG = []
        for num in range(len(lables) + 2):
            checkBoxsAnswOG.append(IntVar())
            checkBoxsOG.append(Checkbutton(self, text=" ", variable = checkBoxsAnswOG[num]))
            checkBoxsOG[num].place(x = 0, y = 115 + (30 * num)) # ohwefioheoifehiofehfoiehfioehfioefheoifheoifheiohfeoifheiowf

        also_label = tk.Label(self, text="Also include: ", font=("Courier", 18))
        also_label.place(x = 450, y = 280)

        checkBoxsAnsw = []
        for num in range(12):
            checkBoxsAnsw.append(IntVar())
        checkBoxs.append(Checkbutton(self, text="City", variable = checkBoxsAnsw[0]))
        checkBoxs.append(Checkbutton(self, text="Team Name", variable = checkBoxsAnsw[1]))
        checkBoxs.append(Checkbutton(self, text="League", variable = checkBoxsAnsw[2]))
        checkBoxs.append(Checkbutton(self, text="Division", variable = checkBoxsAnsw[3]))
        checkBoxs.append(Checkbutton(self, text="General Manager", variable = checkBoxsAnsw[4]))
        checkBoxs.append(Checkbutton(self, text="Manger", variable = checkBoxsAnsw[5]))
        checkBoxs.append(Checkbutton(self, text="Home Stadium", variable = checkBoxsAnsw[6]))
        checkBoxs.append(Checkbutton(self, text="Stadium Capacity", variable = checkBoxsAnsw[7]))
        checkBoxs.append(Checkbutton(self, text="Stadium Year", variable = checkBoxsAnsw[8]))
        checkBoxs.append(Checkbutton(self, text="Address", variable =checkBoxsAnsw[9]))
        checkBoxs.append(Checkbutton(self, text="Phone Number", variable = checkBoxsAnsw[10]))
        checkBoxs.append(Checkbutton(self, text="Website", variable = checkBoxsAnsw[11]))

        for num in range(12):
            checkBoxs[num].place(x = 450, y = 300 + (20 * num))
        for num in range(len(lables)):
            gp_variable = StringVar(self)
            gp_variable.set("") # default value
            lablesVariables.append(gp_variable)
            gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
            lablesOptions.append(gp_options)
            lablesOptions[num].place(x = 160, y = 180 + (30 * num))
            gp_input = Text(self, height = 1, width = 5)
            lableInput.append(gp_input)
            lableInput[num].place(x = 220, y = 180 + (30 * num))
            lables[num].place(x = 35, y = 175 + (30*num))

        batting_go_button = tk.Button(self, text="GO!", command=lambda: [controller.show_frame(StartPage),batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name,lables, checkBoxsAnswOG, checkBoxsAnsw)])
        batting_go_button.place(x = 620, y = 650)


        selectALL = tk.Button(self, text=" Select All ", command=lambda:  select_all(checkBoxs,checkBoxsOG))
        selectALL.place(x = 450, y = 130)
        deselectALL = tk.Button(self, text="De Select All", command=lambda:  deselect_all(checkBoxs,checkBoxsOG))
        deselectALL.place(x = 450, y = 160)
        main_button = tk.Button(self, text="Back to Main", command=lambda: [controller.show_frame(StartPage),clear_batting_pitching_fielding(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, checkBoxs, checkBoxsOG)])
        main_button.place(x = 280, y = 700)

        clear_button = tk.Button(self, text="Clear all", command=lambda: clear_batting_pitching_fielding(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, checkBoxs, checkBoxsOG))
        clear_button.place(x = 450, y = 100)

class PagePitching(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pitching Filters", font=("Courier", 30))
        label.place(x = 200, y = 0)    
        name = "pitching"

        fname_label = tk.Label(self, text="First name: ", font=("Courier", 18))
        fname_label.place(x = 35, y = 55)

        fname_input = Text(self, height = 1, width = 30)
        fname_input.place(x = 160, y = 60)

        lname_label = tk.Label(self, text="Last name: ", font=("Courier", 18))
        lname_label.place(x = 35, y = 85)

        lname_input = Text(self, height = 1, width = 30)
        lname_input.place(x = 160, y = 90)

        position_label = tk.Label(self, text="Position: ", font=("Courier", 18))
        position_label.place(x = 35, y = 115)

        position_variable = StringVar(self)
        position_variable.set("") # default value
        position_options = OptionMenu(self, position_variable, "", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
        position_options.place(x = 160, y = 120)

        team_label = tk.Label(self, text="Team: ", font=("Courier", 18))
        team_label.place(x = 35, y = 145)

        team_variable = StringVar(self)
        team_variable.set("") # default value
        team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
        team_options.place(x = 160, y = 150)

        lables = [] 
        checkBoxs = []
        checkBoxsOG = []
        lablesVariables = [] 
        lablesOptions = []
        lableInput = []

        lables.append(tk.Label(self, text="GP", font=("Courier", 18)))
        lables.append(tk.Label(self, text="GS", font=("Courier", 18)))
        lables.append(tk.Label(self, text="IP", font=("Courier", 18)))
        lables.append(tk.Label(self, text="W", font=("Courier", 18)))
        lables.append(tk.Label(self, text="L", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SV", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SVO", font=("Courier", 18)))
        lables.append(tk.Label(self, text="H", font=("Courier", 18)))
        lables.append(tk.Label(self, text="R", font=("Courier", 18)))
        lables.append(tk.Label(self, text="HR", font=("Courier", 18)))
        lables.append(tk.Label(self, text="ER", font=("Courier", 18)))
        lables.append(tk.Label(self, text="ERA", font=("Courier", 18)))
        lables.append(tk.Label(self, text="BB", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SO", font=("Courier", 18)))
        lables.append(tk.Label(self, text="TP", font=("Courier", 18)))
        lables.append(tk.Label(self, text="WHIP", font=("Courier", 18)))

        # Checkboxes
        also_label = tk.Label(self, text="Also include: ", font=("Courier", 18))
        also_label.place(x = 450, y = 280)

        checkBoxsAnsw = []
        for num in range(12):
            checkBoxsAnsw.append(IntVar())
        checkBoxs.append(Checkbutton(self, text="City", variable = checkBoxsAnsw[0]))
        checkBoxs.append(Checkbutton(self, text="Team Name", variable = checkBoxsAnsw[1]))
        checkBoxs.append(Checkbutton(self, text="League", variable = checkBoxsAnsw[2]))
        checkBoxs.append(Checkbutton(self, text="Division", variable = checkBoxsAnsw[3]))
        checkBoxs.append(Checkbutton(self, text="General Manager", variable = checkBoxsAnsw[4]))
        checkBoxs.append(Checkbutton(self, text="Manger", variable = checkBoxsAnsw[5]))
        checkBoxs.append(Checkbutton(self, text="Home Stadium", variable = checkBoxsAnsw[6]))
        checkBoxs.append(Checkbutton(self, text="Stadium Capacity", variable = checkBoxsAnsw[7]))
        checkBoxs.append(Checkbutton(self, text="Stadium Year", variable = checkBoxsAnsw[8]))
        checkBoxs.append(Checkbutton(self, text="Address", variable =checkBoxsAnsw[9]))
        checkBoxs.append(Checkbutton(self, text="Phone Number", variable = checkBoxsAnsw[10]))
        checkBoxs.append(Checkbutton(self, text="Website", variable = checkBoxsAnsw[11]))

        checkBoxsAnswOG = []
        for num in range(len(lables) + 2):
            checkBoxsAnswOG.append(IntVar())
            checkBoxsOG.append(Checkbutton(self, text=" ", variable = checkBoxsAnswOG[num]))
            checkBoxsOG[num].place(x = 0, y = 115 + (30 * num)) # hefgiouehwfioewhfioehfoiehfioehfeiohfeiohfoiehfoiefheoifheiofwhieo
        for num in range(12):
            checkBoxs[num].place(x = 450, y = 300 + (20 * num))
        for num in range(len(lables)):
            gp_variable = StringVar(self)
            gp_variable.set("") # default value
            lablesVariables.append(gp_variable)
            gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
            lablesOptions.append(gp_options)
            lablesOptions[num].place(x = 160, y = 180 + (30 * num))
            gp_input = Text(self, height = 1, width = 5)
            lableInput.append(gp_input)
            lableInput[num].place(x = 220, y = 180 + (30 * num))
            lables[num].place(x = 35, y = 175 + (30*num))

        batting_go_button = tk.Button(self, text="GO!", command=lambda: [controller.show_frame(StartPage),batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name, lables, checkBoxsAnswOG, checkBoxsAnsw)])
        batting_go_button.place(x = 620, y = 650)
        selectALL = tk.Button(self, text=" Select All ", command=lambda:  select_all(checkBoxs,checkBoxsOG))
        selectALL.place(x = 450, y = 130)
        deselectALL = tk.Button(self, text="De Select All", command=lambda:  deselect_all(checkBoxs,checkBoxsOG))
        deselectALL.place(x = 450, y = 160)
        main_button = tk.Button(self, text="Back to Main", command=lambda: [controller.show_frame(StartPage),clear_batting_pitching_fielding(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, checkBoxs, checkBoxsOG)])
        main_button.place(x = 280, y = 700)

        clear_button = tk.Button(self, text="Clear all", command=lambda: clear_batting_pitching_fielding(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, checkBoxs, checkBoxsOG))
        clear_button.place(x = 450, y = 100)
class PageFielding(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Fielding Filters", font=("Courier", 30))
        label.place(x = 185, y = 0)
        name = "fielding"

        fname_label = tk.Label(self, text="First name: ", font=("Courier", 18))
        fname_label.place(x = 35, y = 55)

        fname_input = Text(self, height = 1, width = 30)
        fname_input.place(x = 160, y = 60)

        lname_label = tk.Label(self, text="Last name: ", font=("Courier", 18))
        lname_label.place(x = 35, y = 85)

        lname_input = Text(self, height = 1, width = 30)
        lname_input.place(x = 160, y = 90)

        position_label = tk.Label(self, text="Position: ", font=("Courier", 18))
        position_label.place(x = 35, y = 115)

        position_variable = StringVar(self)
        position_variable.set("") # default value
        position_options = OptionMenu(self, position_variable, "", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
        position_options.place(x = 160, y = 120)

        team_label = tk.Label(self, text="Team: ", font=("Courier", 18))
        team_label.place(x = 35, y = 145)

        team_variable = StringVar(self)
        team_variable.set("") # default value
        team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
        team_options.place(x = 160, y = 150)

        lables = [] 
        checkBoxs = []
        checkBoxsOG = []
        lablesVariables = [] 
        lablesOptions = []
        lableInput = []

        lables.append(tk.Label(self, text="GP", font=("Courier", 18)))
        lables.append(tk.Label(self, text="GS", font=("Courier", 18)))
        lables.append(tk.Label(self, text="FULL", font=("Courier", 18)))
        lables.append(tk.Label(self, text="TC", font=("Courier", 18)))
        lables.append(tk.Label(self, text="PO", font=("Courier", 18)))
        lables.append(tk.Label(self, text="A", font=("Courier", 18)))
        lables.append(tk.Label(self, text="E", font=("Courier", 18)))
        lables.append(tk.Label(self, text="DP", font=("Courier", 18)))
        lables.append(tk.Label(self, text="FPCT", font=("Courier", 18)))
        lables.append(tk.Label(self, text="RF", font=("Courier", 18)))
        lables.append(tk.Label(self, text="DWAR", font=("Courier", 18)))
        lables.append(tk.Label(self, text="PB", font=("Courier", 18)))
        lables.append(tk.Label(self, text="CSB", font=("Courier", 18)))
        lables.append(tk.Label(self, text="CS", font=("Courier", 18)))
        lables.append(tk.Label(self, text="CSPCT", font=("Courier", 18)))

        # Checkboxes
        also_label = tk.Label(self, text="Also include: ", font=("Courier", 18))
        also_label.place(x = 450, y = 280)

        checkBoxsAnsw = []
        for num in range(12):
            checkBoxsAnsw.append(IntVar())
        checkBoxs.append(Checkbutton(self, text="City", variable = checkBoxsAnsw[0]))
        checkBoxs.append(Checkbutton(self, text="Team Name", variable = checkBoxsAnsw[1]))
        checkBoxs.append(Checkbutton(self, text="League", variable = checkBoxsAnsw[2]))
        checkBoxs.append(Checkbutton(self, text="Division", variable = checkBoxsAnsw[3]))
        checkBoxs.append(Checkbutton(self, text="General Manager", variable = checkBoxsAnsw[4]))
        checkBoxs.append(Checkbutton(self, text="Manger", variable = checkBoxsAnsw[5]))
        checkBoxs.append(Checkbutton(self, text="Home Stadium", variable = checkBoxsAnsw[6]))
        checkBoxs.append(Checkbutton(self, text="Stadium Capacity", variable = checkBoxsAnsw[7]))
        checkBoxs.append(Checkbutton(self, text="Stadium Year", variable = checkBoxsAnsw[8]))
        checkBoxs.append(Checkbutton(self, text="Address", variable =checkBoxsAnsw[9]))
        checkBoxs.append(Checkbutton(self, text="Phone Number", variable = checkBoxsAnsw[10]))
        checkBoxs.append(Checkbutton(self, text="Website", variable = checkBoxsAnsw[11]))

        checkBoxsAnswOG = []
        for num in range(len(lables) + 2):
            checkBoxsAnswOG.append(IntVar())
            checkBoxsOG.append(Checkbutton(self, text=" ", variable = checkBoxsAnswOG[num]))
            checkBoxsOG[num].place(x = 0, y = 115 + (30 * num)) # woeufhewuoifheuiwfhoeifheoihfioehfioehfiohewoifheiofheiofheiofhioew
        for num in range(12):
            checkBoxs[num].place(x = 450, y = 300 + (20 * num))
        for num in range(len(lables)):
            gp_variable = StringVar(self)
            gp_variable.set("") # default value
            lablesVariables.append(gp_variable)
            gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
            lablesOptions.append(gp_options)
            lablesOptions[num].place(x = 160, y = 180 + (30 * num))
            gp_input = Text(self, height = 1, width = 5)
            lableInput.append(gp_input)
            lableInput[num].place(x = 220, y = 180 + (30 * num))
            lables[num].place(x = 35, y = 175 + (30*num))

        batting_go_button = tk.Button(self, text="GO!", command=lambda: [controller.show_frame(StartPage),batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name, lables, checkBoxsAnswOG, checkBoxsAnsw)])
        batting_go_button.place(x = 620, y = 650)

        selectALL = tk.Button(self, text=" Select All ", command=lambda:  select_all(checkBoxs,checkBoxsOG))
        selectALL.place(x = 450, y = 130)
        deselectALL = tk.Button(self, text="De Select All", command=lambda:  deselect_all(checkBoxs,checkBoxsOG))
        deselectALL.place(x = 450, y = 160)
        main_button = tk.Button(self, text="Back to Main", command=lambda: [controller.show_frame(StartPage),clear_batting_pitching_fielding(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, checkBoxs, checkBoxsOG)])
        main_button.place(x = 280, y = 700)

        clear_button = tk.Button(self, text="Clear all", command=lambda: clear_batting_pitching_fielding(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, checkBoxs, checkBoxsOG))
        clear_button.place(x = 450, y = 100)

class PagePirates(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="View a Current Pirates Player:", font=("Courier", 20))
        label1.place(x = 170, y = 0)

        divider1 = tk.Label(self, text="______________________________________", font=("Courier", 30))
        divider1.place(x = 0, y = 200)

        filters_label = tk.Label(self, text="Pirates 2021 Roster Filters:", font=("Courier", 20))
        filters_label.place(x = 190, y = 240)

        divider2 = tk.Label(self, text="______________________________________", font=("Courier", 30))
        divider2.place(x = 0, y = 440)

        filters_label = tk.Label(self, text="Pirates 2021 Schedule Filters:", font=("Courier", 20))
        filters_label.place(x = 190, y = 480)


        # ------ Section 1 -------
        player_label = tk.Label(self, text="Select a player:", font=("Courier", 18))
        player_label.place(x = 80, y = 80)

        player_variable = StringVar(self)
        player_variable.set("") # default value
        player_options = OptionMenu(self, player_variable, "", "Tanner Anderson", "Anthony Banda", "David Bednar", "Steven Brault", "J.T. Brubaker", "Blake Cederlind", "Roansy Contreras", "Wil Crowe", "Eric Hanhold", "Sam Howard", "Mitch Keller", "Max Kranick", "Chad Kuhl", "Nick Mears", "Luis Oviedo", "Dillon Peters", "Cody Ponce", "Chris Stratton", "Duane Underwood Jr.", "Bryse Wilson", "Miguel Yajure", "Taylor Davis", "Michael Perez", "Jacob Stallings", "Diego Castillo", "Rodolfo Castro", "Michael Chavis", "Oneil Cruz", "Ke'Bryan Hayes", "Tucupita Marcano", "Colin Moran", "Kevin Newman", "Hoy Park", "Cole Tucker", "Anthony Alford", "Greg Allen", "Phillip Evans", "Ben Gamel", "Jared Oliva", "Bryan Reynolds")
        player_options.place(x = 80, y = 110)

        action_label = tk.Label(self, text="Select an action:", font=("Courier", 18))
        action_label.place(x = 400, y = 80)

        stats_button = tk.Button(self, text="Stats", command=lambda: controller.show_frame(StartPage))
        stats_button.place(x = 400, y = 120)

        profile_button = tk.Button(self, text="Profile", command=lambda: controller.show_frame(StartPage))
        profile_button.place(x = 400, y = 170)

        highlights_button = tk.Button(self, text="Highlights", command=lambda: controller.show_frame(StartPage))
        highlights_button.place(x = 490, y = 120)

        music_button = tk.Button(self, text="Music", command=lambda: controller.show_frame(StartPage))
        music_button.place(x = 490, y = 170)


        # ------ Section 2 -------
        position_label = tk.Label(self, text="Position: ", font=("Courier", 18))
        position_label.place(x = 30, y = 315)

        position_variable = StringVar(self)
        position_variable.set("") # default value
        position_options = OptionMenu(self, position_variable, "", "Pitcher", "Catcher", "Infielder", "Outfielder")
        position_options.place(x = 160, y = 320)

        bats_label = tk.Label(self, text="Bats: ", font=("Courier", 18))
        bats_label.place(x = 30, y = 345)

        bats_variable = StringVar(self)
        bats_variable.set("") # default value
        bats_options = OptionMenu(self, bats_variable, "", "Left", "Right", "Switch")
        bats_options.place(x = 160, y = 350)

        throws_label = tk.Label(self, text="Throws: ", font=("Courier", 18))
        throws_label.place(x = 30, y = 375)

        throws_variable = StringVar(self)
        throws_variable.set("") # default value
        throws_options = OptionMenu(self, throws_variable, "", "Left", "Right")
        throws_options.place(x = 160, y = 380)

        checkboxes_label = tk.Label(self, text="Also Include: ", font=("Courier", 18))
        checkboxes_label.place(x = 400, y = 305)

        rostercheckBoxs = []
        rostercheckBoxsAnsw = []
        for num in range(5):
            rostercheckBoxsAnsw.append(IntVar())
        rostercheckBoxs.append(Checkbutton(self, text="Jersey Number", variable = rostercheckBoxsAnsw[0]))
        rostercheckBoxs.append(Checkbutton(self, text="Height", variable = rostercheckBoxsAnsw[1]))
        rostercheckBoxs.append(Checkbutton(self, text="Weight", variable = rostercheckBoxsAnsw[2]))
        rostercheckBoxs.append(Checkbutton(self, text="Date of Birth", variable = rostercheckBoxsAnsw[3]))
        rostercheckBoxs.append(Checkbutton(self, text="2021 Stats", variable = rostercheckBoxsAnsw[4]))

        for num in range(5):
            rostercheckBoxs[num].place(x = 400, y = 330 + (20 * num))

        roster_go_button = tk.Button(self, text="GO!", command=lambda: [controller.show_frame(StartPage),batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name, lables, checkBoxsAnswOG, checkBoxsAnsw)])
        roster_go_button.place(x = 600, y = 400)

        # ------ Section 3 -------
        location_label = tk.Label(self, text="Location: ", font=("Courier", 18))
        location_label.place(x = 30, y = 515)

        location_variable = StringVar(self)
        location_variable.set("") # default value
        location_options = OptionMenu(self, location_variable, "", "Home", "Away")
        location_options.place(x = 160, y = 518)

        opp_label = tk.Label(self, text="Opponent: ", font=("Courier", 18))
        opp_label.place(x = 30, y = 545)

        opp_variable = StringVar(self)
        opp_variable.set("") # default value
        opp_options = OptionMenu(self, opp_variable, "", "ARI", "ATL", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "KCR", "LAD", "MIA", "MIL", "MIN", "NYM", "PHI", "SDP", "SFG", "STL", "WAS")
        opp_options.place(x = 160, y = 548)

        result_label = tk.Label(self, text="Result: ", font=("Courier", 18))
        result_label.place(x = 30, y = 575)

        result_variable = StringVar(self)
        result_variable.set("") # default value
        result_options = OptionMenu(self, result_variable, "", "Win", "Loss")
        result_options.place(x = 160, y = 578)

        rdiff_label = tk.Label(self, text="Run Diff: ", font=("Courier", 18))
        rdiff_label.place(x = 30, y = 605)

        rdiff_variable = StringVar(self)
        rdiff_variable.set("") # default value
        rdiff_options = OptionMenu(self, rdiff_variable, "", "-19", "-13", "-12", "-11", "-10", "-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1", "1", "2", "3", "4", "5", "6", "7", "8", "10")
        rdiff_options.place(x = 160, y = 608)

        inn_label = tk.Label(self, text="Innings: ", font=("Courier", 18))
        inn_label.place(x = 30, y = 635)

        inn_variable = StringVar(self)
        inn_variable.set("") # default value
        inn_options = OptionMenu(self, inn_variable, "", "7", "8", "9", "9+")
        inn_options.place(x = 160, y = 638)

        checkboxes_label = tk.Label(self, text="Also Include: ", font=("Courier", 18))
        checkboxes_label.place(x = 300, y = 525)

        schedulecheckBoxs = []
        schedulecheckBoxsAnsw = []
        for num in range(15):
            schedulecheckBoxsAnsw.append(IntVar())
        schedulecheckBoxs.append(Checkbutton(self, text="Date", variable = schedulecheckBoxsAnsw[0]))
        schedulecheckBoxs.append(Checkbutton(self, text="Runs Scored", variable = schedulecheckBoxsAnsw[1]))
        schedulecheckBoxs.append(Checkbutton(self, text="Runs Against", variable = schedulecheckBoxsAnsw[2]))
        schedulecheckBoxs.append(Checkbutton(self, text="Record", variable = schedulecheckBoxsAnsw[3]))
        schedulecheckBoxs.append(Checkbutton(self, text="Division rank", variable = schedulecheckBoxsAnsw[4]))
        schedulecheckBoxs.append(Checkbutton(self, text="Games Back", variable = schedulecheckBoxsAnsw[5]))
        schedulecheckBoxs.append(Checkbutton(self, text="Winning Pitcher", variable = schedulecheckBoxsAnsw[6]))
        schedulecheckBoxs.append(Checkbutton(self, text="Losing Pitcher", variable = schedulecheckBoxsAnsw[7]))
        schedulecheckBoxs.append(Checkbutton(self, text="Save", variable = schedulecheckBoxsAnsw[8]))
        schedulecheckBoxs.append(Checkbutton(self, text="Time", variable = schedulecheckBoxsAnsw[9]))
        schedulecheckBoxs.append(Checkbutton(self, text="Day/Night", variable = schedulecheckBoxsAnsw[10]))
        schedulecheckBoxs.append(Checkbutton(self, text="Attendance", variable = schedulecheckBoxsAnsw[11]))
        schedulecheckBoxs.append(Checkbutton(self, text="CLI", variable = schedulecheckBoxsAnsw[12]))
        schedulecheckBoxs.append(Checkbutton(self, text="Streak", variable = schedulecheckBoxsAnsw[13]))
        schedulecheckBoxs.append(Checkbutton(self, text="Boxscore", variable = schedulecheckBoxsAnsw[14]))

        for num in range(0, 5):
            schedulecheckBoxs[num].place(x = 250, y = 560 + (20 * num))

        count = 0
        for num1 in range(5, 10):
            schedulecheckBoxs[num1].place(x = 360, y = 560 + (20 * count))
            count += 1

        count = 0
        for num2 in range(10, 15):
            schedulecheckBoxs[num2].place(x = 490, y = 560 + (20 * count))
            count += 1

        schedule_count_button = tk.Button(self, text="Count!", command=lambda: [controller.show_frame(StartPage),batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name, lables, checkBoxsAnswOG, checkBoxsAnsw)])
        schedule_count_button.place(x = 600, y = 600)

        schedule_go_button = tk.Button(self, text="GO!", command=lambda: [controller.show_frame(StartPage),batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name, lables, checkBoxsAnswOG, checkBoxsAnsw)])
        schedule_go_button.place(x = 600, y = 630)

        main_button = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        main_button.place(x = 220, y = 700)

        clear_button = tk.Button(self, text="Clear All", command=lambda: controller.show_frame(StartPage))
        clear_button.place(x = 340, y = 700)
        

app = Baseball()
app.mainloop()