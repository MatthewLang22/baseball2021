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
    for num in range(10):
        checkBoxs[num].deselect()
    for num in range(len(lablesVariables)):
        lablesVariables[num].set("")
        gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
        lablesOptions[num]= gp_options
        lableInput[num].delete('1.0', END)
        checkBoxsOG[num].deselect()
def batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name):
    querey = ("SELECT * from " + name  + " INNER JOIN teams ON (" + name + ".TEAM = teams.TEAM)" + " where ")
    count = 0
    if(fname_input.get("1.0",'end-1c') != ""):
        querey += ("FNAME = " + "\'" + fname_input.get("1.0",'end-1c') + "\'")
        count += 1
    if(lname_input.get("1.0",'end-1c') != ""):
        if(count != 0):
            querey += " AND LNAME = "
            querey += ("\'" +lname_input.get("1.0",'end-1c') + "\'")
        else:
            count += 1
            querey += (" LNAME = " + "\'" + lname_input.get("1.0",'end-1c') + "\'")
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

        Button(self, text = 'Click Me !', image = exit_pic, command = self.destroy).pack()


class PageBatting(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Batting Filters", font=("Courier", 30))
        label.place(x = 200, y = 0)    
        name = "batting"

        fname_label = tk.Label(self, text="First name: ", font=("Courier", 18))
        fname_label.place(x = 25, y = 55)

        fname_input = Text(self, height = 1, width = 30)
        fname_input.place(x = 160, y = 60)

        lname_label = tk.Label(self, text="Last name: ", font=("Courier", 18))
        lname_label.place(x = 25, y = 85)

        lname_input = Text(self, height = 1, width = 30)
        lname_input.place(x = 160, y = 90)

        position_label = tk.Label(self, text="Position: ", font=("Courier", 18))
        position_label.place(x = 25, y = 115)

        position_variable = StringVar(self)
        position_variable.set("") # default value
        position_options = OptionMenu(self, position_variable, "", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
        position_options.place(x = 160, y = 115)

        team_label = tk.Label(self, text="Team: ", font=("Courier", 18))
        team_label.place(x = 25, y = 145)

        team_variable = StringVar(self)
        team_variable.set("") # default value
        team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
        team_options.place(x = 160, y = 145)

        lables = [] 
        checkBoxsOG = []
        checkBoxs = []
        lablesVariables = [] 
        lablesOptions = []
        lableInput = []

        lables.append(tk.Label(self, text="GP: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="AVG: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="AB: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="R: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="H: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="2B: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="3B: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="HR: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="RBI: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SB: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="CS: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="BB: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SO: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="OBP: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SLG: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="OPS: ", font=("Courier", 18)))

        # Checkboxes
        for num in range(len(lables) + 2):
            checkBoxsOG.append(Checkbutton(self, text=" ", variable = IntVar()))
            checkBoxsOG[num].place(x = 0, y = 120 + (30 * num))

        also_label = tk.Label(self, text="Also include: ", font=("Courier", 18))
        also_label.place(x = 450, y = 280)

        checkBoxs.append(Checkbutton(self, text="City", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Team Name", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="League", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Division", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="General Manager", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Manger", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Home Stadium", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Stadium Capacity", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Stadium Year", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Address", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Phone Number", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Website", variable = IntVar()))

        for num in range(10):
            checkBoxs[num].place(x = 450, y = 300 + (20 * num))
        for num in range(len(lables)):
            gp_variable = StringVar(self)
            gp_variable.set("") # default value
            lablesVariables.append(gp_variable)
            gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
            lablesOptions.append(gp_options)
            lablesOptions[num].place(x = 160, y = 175 + (30 * num))
            gp_input = Text(self, height = 1, width = 5)
            lableInput.append(gp_input)
            lableInput[num].place(x = 210, y = 180 + (30 * num))
            lables[num].place(x = 25, y = 175 + (30*num))

        batting_go_button = tk.Button(self, text="GO!", command=lambda: [controller.show_frame(StartPage),batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name)])
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
        fname_label.place(x = 25, y = 55)

        fname_input = Text(self, height = 1, width = 30)
        fname_input.place(x = 160, y = 60)

        lname_label = tk.Label(self, text="Last name: ", font=("Courier", 18))
        lname_label.place(x = 25, y = 85)

        lname_input = Text(self, height = 1, width = 30)
        lname_input.place(x = 160, y = 90)

        position_label = tk.Label(self, text="Position: ", font=("Courier", 18))
        position_label.place(x = 25, y = 115)

        position_variable = StringVar(self)
        position_variable.set("") # default value
        position_options = OptionMenu(self, position_variable, "", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
        position_options.place(x = 160, y = 115)

        team_label = tk.Label(self, text="Team: ", font=("Courier", 18))
        team_label.place(x = 25, y = 145)

        team_variable = StringVar(self)
        team_variable.set("") # default value
        team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
        team_options.place(x = 160, y = 145)

        lables = [] 
        checkBoxs = []
        checkBoxsOG = []
        lablesVariables = [] 
        lablesOptions = []
        lableInput = []

        lables.append(tk.Label(self, text="GP: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="GS: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="IP: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="W: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="L: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SV: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SVO: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="H: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="R: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="HR: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="ER: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="ERA: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="BB: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="SO: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="TP: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="WHIP: ", font=("Courier", 18)))

        # Checkboxes
        also_label = tk.Label(self, text="Also include: ", font=("Courier", 18))
        also_label.place(x = 450, y = 280)

        checkBoxs.append(Checkbutton(self, text="City", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Team Name", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="League", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Division", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="General Manager", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Manger", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Home Stadium", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Stadium Capacity", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Stadium Year", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Address", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Phone Number", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Website", variable = IntVar()))

        for num in range(len(lables) + 2):
            checkBoxsOG.append(Checkbutton(self, text=" ", variable = IntVar()))
            checkBoxsOG[num].place(x = 0, y = 120 + (30 * num))
        for num in range(10):
            checkBoxs[num].place(x = 450, y = 300 + (20 * num))
        for num in range(len(lables)):
            gp_variable = StringVar(self)
            gp_variable.set("") # default value
            lablesVariables.append(gp_variable)
            gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
            lablesOptions.append(gp_options)
            lablesOptions[num].place(x = 160, y = 175 + (30 * num))
            gp_input = Text(self, height = 1, width = 5)
            lableInput.append(gp_input)
            lableInput[num].place(x = 210, y = 180 + (30 * num))
            lables[num].place(x = 25, y = 175 + (30*num))

        batting_go_button = tk.Button(self, text="GO!", command=lambda: [controller.show_frame(StartPage),batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name)])
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
        fname_label.place(x = 25, y = 55)

        fname_input = Text(self, height = 1, width = 30)
        fname_input.place(x = 160, y = 60)

        lname_label = tk.Label(self, text="Last name: ", font=("Courier", 18))
        lname_label.place(x = 25, y = 85)

        lname_input = Text(self, height = 1, width = 30)
        lname_input.place(x = 160, y = 90)

        position_label = tk.Label(self, text="Position: ", font=("Courier", 18))
        position_label.place(x = 25, y = 115)

        position_variable = StringVar(self)
        position_variable.set("") # default value
        position_options = OptionMenu(self, position_variable, "", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
        position_options.place(x = 160, y = 115)

        team_label = tk.Label(self, text="Team: ", font=("Courier", 18))
        team_label.place(x = 25, y = 145)

        team_variable = StringVar(self)
        team_variable.set("") # default value
        team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
        team_options.place(x = 160, y = 145)

        lables = [] 
        checkBoxs = []
        checkBoxsOG = []
        lablesVariables = [] 
        lablesOptions = []
        lableInput = []

        lables.append(tk.Label(self, text="GP: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="GS: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="FULL: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="TC: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="PO: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="A: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="E: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="DP: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="FPCT: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="RF: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="DWAR: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="PB: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="CSB: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="CS: ", font=("Courier", 18)))
        lables.append(tk.Label(self, text="CSPCT: ", font=("Courier", 18)))

        # Checkboxes
        also_label = tk.Label(self, text="Also include: ", font=("Courier", 18))
        also_label.place(x = 450, y = 280)

        checkBoxs.append(Checkbutton(self, text="City", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Team Name", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="League", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Division", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="General Manager", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Manger", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Home Stadium", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Stadium Capacity", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Stadium Year", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Address", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Phone Number", variable = IntVar()))
        checkBoxs.append(Checkbutton(self, text="Website", variable = IntVar()))

        for num in range(len(lables) + 2):
            checkBoxsOG.append(Checkbutton(self, text=" ", variable = IntVar()))
            checkBoxsOG[num].place(x = 0, y = 120 + (30 * num))
        for num in range(10):
            checkBoxs[num].place(x = 450, y = 300 + (20 * num))
        for num in range(len(lables)):
            gp_variable = StringVar(self)
            gp_variable.set("") # default value
            lablesVariables.append(gp_variable)
            gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
            lablesOptions.append(gp_options)
            lablesOptions[num].place(x = 160, y = 175 + (30 * num))
            gp_input = Text(self, height = 1, width = 5)
            lableInput.append(gp_input)
            lableInput[num].place(x = 210, y = 180 + (30 * num))
            lables[num].place(x = 25, y = 175 + (30*num))

        batting_go_button = tk.Button(self, text="GO!", command=lambda: [controller.show_frame(StartPage),batting_pitching_fielding_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options, name)])
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

        label1 = tk.Label(self, text="View a Pirates Player:", font=("Courier", 20))
        label1.place(x = 210, y = 0)

        divider1 = tk.Label(self, text="______________________________________", font=("Courier", 30))
        divider1.place(x = 0, y = 200)

        filters_label = tk.Label(self, text="Pirates 2021 Roster Filters:", font=("Courier", 20))
        filters_label.place(x = 190, y = 240)

        divider2 = tk.Label(self, text="______________________________________", font=("Courier", 30))
        divider2.place(x = 0, y = 440)

        filters_label = tk.Label(self, text="Pirates 2021 Schedule Filters:", font=("Courier", 20))
        filters_label.place(x = 190, y = 480)

        player_label = tk.Label(self, text="Select a player:", font=("Courier", 18))
        player_label.place(x = 80, y = 80)

        player_variable = StringVar(self)
        player_variable.set("") # default value
        player_options = OptionMenu(self, player_variable, "", "Tanner Anderson", "Anthony Banda", "David Bednar", "Steven Brault", "J.T. Brubaker", "Blake Cederlind", "Roansy Contreras", "Wil Crowe", "Eric Hanhold", "Sam Howard", "Mitch Keller", "Max Kranick", "Chad Kuhl", "Nick Mears", "Luis Oviedo", "Dillon Peters", "Cody Ponce", "Chris Stratton", "Duane Underwood Jr.", "Bryse Wilson", "Miguel Yajure", "Taylor Davis", "Michael Perez", "Jacob Stallings", "Diego Castillo", "Rodolfo Castro", "Michael Chavis", "Oneil Cruz", "Ke'Bryan Hayes", "Tucupita Marcano", "Colin Moran", "Kevin Newman", "Hoy Park", "Cole Tucker", "Anthony Alford", "Greg Allen", "Phillip Evans", "Ben Gamel", "Jared Oliva", "Bryan Reynolds")
        player_options.place(x = 80, y = 110)

        action_label = tk.Label(self, text="Select an action:", font=("Courier", 18))
        action_label.place(x = 400, y = 80)

        profile_button = tk.Button(self, text="Profile", command=lambda: controller.show_frame(StartPage))
        profile_button.place(x = 400, y = 120)

        stats_button = tk.Button(self, text="Stats", command=lambda: controller.show_frame(StartPage))
        stats_button.place(x = 400, y = 170)

        highlights_button = tk.Button(self, text="Highlights", command=lambda: controller.show_frame(StartPage))
        highlights_button.place(x = 490, y = 120)

        music_button = tk.Button(self, text="Music", command=lambda: controller.show_frame(StartPage))
        music_button.place(x = 490, y = 170)

        main_button = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        main_button.place(x = 280, y = 700)
        

app = Baseball()
app.mainloop()