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

def clear_batting(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options):
    fname_input.delete('1.0', END)
    lname_input.delete('1.0', END)
    position_variable.set("") # default value
    position_options = OptionMenu(self, position_variable, "", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
    team_variable.set("")
    team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")

    for num in range(16):
        lablesVariables[num].set("")
        gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
        lablesOptions[num]= gp_options
        lableInput[num].delete('1.0', END)
def batting_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options):
    querey = "SELECT * from batting where "
    count = 0
    if(fname_input.get("1.0",'end-1c') != ""):
        querey += ("FNAME = " + "\'" + fname_input.get("1.0",'end-1c') + "\'")
        count += 1
    if(lname_input.get("1.0",'end-1c') != ""):
        if( count != 0):
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
        position_options.place(x = 160, y = 120)

        team_label = tk.Label(self, text="Team: ", font=("Courier", 18))
        team_label.place(x = 25, y = 145)

        team_variable = StringVar(self)
        team_variable.set("") # default value
        team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
        team_options.place(x = 160, y = 150)

        lables = [] 
        lablesVariables = [] 
        lablesOptions = []
        lableInput = []

        gp_label = tk.Label(self, text="GP: ", font=("Courier", 18))
        lables.append(gp_label)
        avg_label = tk.Label(self, text="AVG: ", font=("Courier", 18))
        lables.append(avg_label)
        ab_label = tk.Label(self, text="AB: ", font=("Courier", 18))
        lables.append(ab_label)
        r_label = tk.Label(self, text="R: ", font=("Courier", 18))
        lables.append(r_label)
        h_label = tk.Label(self, text="H: ", font=("Courier", 18))
        lables.append(h_label)
        b2_label = tk.Label(self, text="2B: ", font=("Courier", 18))
        lables.append(b2_label)
        b3_label = tk.Label(self, text="3B: ", font=("Courier", 18))
        lables.append(b3_label)
        hr_label = tk.Label(self, text="HR: ", font=("Courier", 18))
        lables.append(hr_label)
        rbi_label = tk.Label(self, text="RBI: ", font=("Courier", 18))
        lables.append(rbi_label)
        sb_label = tk.Label(self, text="SB: ", font=("Courier", 18))
        lables.append(sb_label)
        cs_label = tk.Label(self, text="CS: ", font=("Courier", 18))
        lables.append(cs_label)
        bb_label = tk.Label(self, text="BB: ", font=("Courier", 18))
        lables.append(bb_label)
        so_label = tk.Label(self, text="SO: ", font=("Courier", 18))
        lables.append(so_label)
        obp_label = tk.Label(self, text="OBP: ", font=("Courier", 18))
        lables.append(obp_label)
        slg_label = tk.Label(self, text="SLG: ", font=("Courier", 18))
        lables.append(slg_label)
        ops_label = tk.Label(self, text="OPS: ", font=("Courier", 18))
        lables.append(ops_label)

        for num in range(16):
            gp_variable = StringVar(self)
            gp_variable.set("") # default value
            lablesVariables.append(gp_variable)
            gp_options = OptionMenu(self, lablesVariables[num], "", "=", "<", ">")
            lablesOptions.append(gp_options)
            lablesOptions[num].place(x = 160, y = 180 + (30 * num))
            gp_input = Text(self, height = 1, width = 5)
            lableInput.append(gp_input)
            lableInput[num].place(x = 210, y = 180 + (30 * num))
            lables[num].place(x = 25, y = 175 + (30*num))

        batting_go_button = tk.Button(self, text="GO!", command=lambda: [controller.show_frame(StartPage),batting_q(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options)])
        batting_go_button.place(x = 620, y = 650)

        main_button = tk.Button(self, text="Back to Main", command=lambda: [controller.show_frame(StartPage),clear_batting(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options)])
        main_button.place(x = 280, y = 700)

        clear_button = tk.Button(self, text="clear", command=lambda: clear_batting(self, lablesVariables,lablesOptions,lableInput, fname_input, lname_input,position_variable,position_options,team_variable, team_options))
        clear_button.place(x = 500, y = 100)

class PagePitching(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pitching Filters", font=("Courier", 30))
        label.place(x = 185, y = 0)

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
        position_options.place(x = 160, y = 120)

        team_label = tk.Label(self, text="Team: ", font=("Courier", 18))
        team_label.place(x = 25, y = 145)

        team_variable = StringVar(self)
        team_variable.set("") # default value
        team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
        team_options.place(x = 160, y = 150)

        gp_label = tk.Label(self, text="GP: ", font=("Courier", 18))
        gp_label.place(x = 25, y = 175)

        gp_variable = StringVar(self)
        gp_variable.set("") # default value
        gp_options = OptionMenu(self, gp_variable, "", "=", "<", ">")
        gp_options.place(x = 160, y = 180)

        gp_input = Text(self, height = 1, width = 5)
        gp_input.place(x = 210, y = 180)

        gs_label = tk.Label(self, text="GS: ", font=("Courier", 18))
        gs_label.place(x = 25, y = 205)

        gs_variable = StringVar(self)
        gs_variable.set("") # default value
        gs_options = OptionMenu(self, gs_variable, "", "=", "<", ">")
        gs_options.place(x = 160, y = 210)

        gs_input = Text(self, height = 1, width = 5)
        gs_input.place(x = 210, y = 210)

        ip_label = tk.Label(self, text="IP: ", font=("Courier", 18))
        ip_label.place(x = 25, y = 235)

        ip_variable = StringVar(self)
        ip_variable.set("") # default value
        ip_options = OptionMenu(self, ip_variable, "", "=", "<", ">")
        ip_options.place(x = 160, y = 240)

        ip_input = Text(self, height = 1, width = 5)
        ip_input.place(x = 210, y = 240)

        w_label = tk.Label(self, text="W: ", font=("Courier", 18))
        w_label.place(x = 25, y = 265)

        w_variable = StringVar(self)
        w_variable.set("") # default value
        w_options = OptionMenu(self, w_variable, "", "=", "<", ">")
        w_options.place(x = 160, y = 270)

        w_input = Text(self, height = 1, width = 5)
        w_input.place(x = 210, y = 270)

        l_label = tk.Label(self, text="L: ", font=("Courier", 18))
        l_label.place(x = 25, y = 295)

        l_variable = StringVar(self)
        l_variable.set("") # default value
        l_options = OptionMenu(self, l_variable, "", "=", "<", ">")
        l_options.place(x = 160, y = 300)

        l_input = Text(self, height = 1, width = 5)
        l_input.place(x = 210, y = 300)

        sv_label = tk.Label(self, text="SV: ", font=("Courier", 18))
        sv_label.place(x = 25, y = 325)

        sv_variable = StringVar(self)
        sv_variable.set("") # default value
        sv_options = OptionMenu(self, sv_variable, "", "=", "<", ">")
        sv_options.place(x = 160, y = 330)

        sv_input = Text(self, height = 1, width = 5)
        sv_input.place(x = 210, y = 330)

        svo_label = tk.Label(self, text="SVO: ", font=("Courier", 18))
        svo_label.place(x = 25, y = 355)

        svo_variable = StringVar(self)
        svo_variable.set("") # default value
        svo_options = OptionMenu(self, svo_variable, "", "=", "<", ">")
        svo_options.place(x = 160, y = 360)

        svo_input = Text(self, height = 1, width = 5)
        svo_input.place(x = 210, y = 360)

        h_label = tk.Label(self, text="H: ", font=("Courier", 18))
        h_label.place(x = 25, y = 385)

        h_variable = StringVar(self)
        h_variable.set("") # default value
        h_options = OptionMenu(self, h_variable, "", "=", "<", ">")
        h_options.place(x = 160, y = 390)

        h_input = Text(self, height = 1, width = 5)
        h_input.place(x = 210, y = 390)

        r_label = tk.Label(self, text="R: ", font=("Courier", 18))
        r_label.place(x = 25, y = 415)

        r_variable = StringVar(self)
        r_variable.set("") # default value
        r_options = OptionMenu(self, r_variable, "", "=", "<", ">")
        r_options.place(x = 160, y = 420)

        r_input = Text(self, height = 1, width = 5)
        r_input.place(x = 210, y = 420)

        hr_label = tk.Label(self, text="HR: ", font=("Courier", 18))
        hr_label.place(x = 25, y = 445)

        hr_variable = StringVar(self)
        hr_variable.set("") # default value
        hr_options = OptionMenu(self, hr_variable, "", "=", "<", ">")
        hr_options.place(x = 160, y = 450)

        hr_input = Text(self, height = 1, width = 5)
        hr_input.place(x = 210, y = 450)

        er_label = tk.Label(self, text="ER: ", font=("Courier", 18))
        er_label.place(x = 25, y = 475)

        er_variable = StringVar(self)
        er_variable.set("") # default value
        er_options = OptionMenu(self, er_variable, "", "=", "<", ">")
        er_options.place(x = 160, y = 480)

        er_input = Text(self, height = 1, width = 5)
        er_input.place(x = 210, y = 480)

        era_label = tk.Label(self, text="ERA: ", font=("Courier", 18))
        era_label.place(x = 25, y = 505)

        era_variable = StringVar(self)
        era_variable.set("") # default value
        era_options = OptionMenu(self, era_variable, "", "=", "<", ">")
        era_options.place(x = 160, y = 510)

        era_input = Text(self, height = 1, width = 5)
        era_input.place(x = 210, y = 510)

        bb_label = tk.Label(self, text="BB: ", font=("Courier", 18))
        bb_label.place(x = 25, y = 535)

        bb_variable = StringVar(self)
        bb_variable.set("") # default value
        bb_options = OptionMenu(self, bb_variable, "", "=", "<", ">")
        bb_options.place(x = 160, y = 540)

        bb_input = Text(self, height = 1, width = 5)
        bb_input.place(x = 210, y = 540)

        so_label = tk.Label(self, text="SO: ", font=("Courier", 18))
        so_label.place(x = 25, y = 565)

        so_variable = StringVar(self)
        so_variable.set("") # default value
        so_options = OptionMenu(self, so_variable, "", "=", "<", ">")
        so_options.place(x = 160, y = 570)

        so_input = Text(self, height = 1, width = 5)
        so_input.place(x = 210, y = 570)

        tp_label = tk.Label(self, text="TP: ", font=("Courier", 18))
        tp_label.place(x = 25, y = 595)

        tp_variable = StringVar(self)
        tp_variable.set("") # default value
        tp_options = OptionMenu(self, tp_variable, "", "=", "<", ">")
        tp_options.place(x = 160, y = 600)

        tp_input = Text(self, height = 1, width = 5)
        tp_input.place(x = 210, y = 600)

        whip_label = tk.Label(self, text="WHIP: ", font=("Courier", 18))
        whip_label.place(x = 25, y = 625)

        whip_variable = StringVar(self)
        whip_variable.set("") # default value
        whip_options = OptionMenu(self, whip_variable, "", "=", "<", ">")
        whip_options.place(x = 160, y = 630)

        whip_input = Text(self, height = 1, width = 5)
        whip_input.place(x = 210, y = 630)

        # Checkboxes
        also_label = tk.Label(self, text="Also include: ", font=("Courier", 18))
        also_label.place(x = 450, y = 280)

        city = Checkbutton(self, text="City", variable = IntVar())
        city.place(x = 450, y = 300)

        nickname = Checkbutton(self, text="Team Name", variable = IntVar())
        nickname.place(x = 450, y = 320)

        league = Checkbutton(self, text="League", variable = IntVar())
        league.place(x = 450, y = 340)

        division = Checkbutton(self, text="Division", variable = IntVar())
        division.place(x = 450, y = 360)

        gm = Checkbutton(self, text="General Manager", variable = IntVar())
        gm.place(x = 450, y = 380)

        man = Checkbutton(self, text="Manger", variable = IntVar())
        man.place(x = 450, y = 400)

        stadium = Checkbutton(self, text="Home Stadium", variable = IntVar())
        stadium.place(x = 450, y = 420)

        cap = Checkbutton(self, text="Stadium Capacity", variable = IntVar())
        cap.place(x = 450, y = 440)

        syear = Checkbutton(self, text="Stadium Year", variable = IntVar())
        syear.place(x = 450, y = 460)

        address = Checkbutton(self, text="Address", variable = IntVar())
        address.place(x = 450, y = 480)

        phone = Checkbutton(self, text="Phone Number", variable = IntVar())
        phone.place(x = 450, y = 500)

        web = Checkbutton(self, text="Website", variable = IntVar())
        web.place(x = 450, y = 520)

        batting_go_button = tk.Button(self, text="GO!", command=lambda: controller.show_frame(StartPage))
        batting_go_button.place(x = 620, y = 650)

        main_button = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        main_button.place(x = 280, y = 700)

class PageFielding(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Fielding Filters", font=("Courier", 30))
        label.place(x = 185, y = 0)

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
        position_options.place(x = 160, y = 120)

        team_label = tk.Label(self, text="Team: ", font=("Courier", 18))
        team_label.place(x = 25, y = 145)

        team_variable = StringVar(self)
        team_variable.set("") # default value
        team_options = OptionMenu(self, team_variable, "", "ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", "HOU" , "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", "PHI", "PIT" , "SDP", "SFG", "SEA", "STL", "TBR", "TEX", "TOR", "WAS")
        team_options.place(x = 160, y = 150)

        gp_label = tk.Label(self, text="GP: ", font=("Courier", 18))
        gp_label.place(x = 25, y = 175)

        gp_variable = StringVar(self)
        gp_variable.set("") # default value
        gp_options = OptionMenu(self, gp_variable, "", "=", "<", ">")
        gp_options.place(x = 160, y = 180)

        gp_input = Text(self, height = 1, width = 5)
        gp_input.place(x = 210, y = 180)

        gs_label = tk.Label(self, text="GS: ", font=("Courier", 18))
        gs_label.place(x = 25, y = 205)

        gs_variable = StringVar(self)
        gs_variable.set("") # default value
        gs_options = OptionMenu(self, gs_variable, "", "=", "<", ">")
        gs_options.place(x = 160, y = 210)

        gs_input = Text(self, height = 1, width = 5)
        gs_input.place(x = 210, y = 210)

        full_label = tk.Label(self, text="FULL: ", font=("Courier", 18))
        full_label.place(x = 25, y = 235)

        full_variable = StringVar(self)
        full_variable.set("") # default value
        full_options = OptionMenu(self, full_variable, "", "=", "<", ">")
        full_options.place(x = 160, y = 240)

        full_input = Text(self, height = 1, width = 5)
        full_input.place(x = 210, y = 240)

        tc_label = tk.Label(self, text="TC: ", font=("Courier", 18))
        tc_label.place(x = 25, y = 265)

        tc_variable = StringVar(self)
        tc_variable.set("") # default value
        tc_options = OptionMenu(self, tc_variable, "", "=", "<", ">")
        tc_options.place(x = 160, y = 270)

        tc_input = Text(self, height = 1, width = 5)
        tc_input.place(x = 210, y = 270)

        po_label = tk.Label(self, text="PO: ", font=("Courier", 18))
        po_label.place(x = 25, y = 295)

        po_variable = StringVar(self)
        po_variable.set("") # default value
        po_options = OptionMenu(self, po_variable, "", "=", "<", ">")
        po_options.place(x = 160, y = 300)

        po_input = Text(self, height = 1, width = 5)
        po_input.place(x = 210, y = 300)

        a_label = tk.Label(self, text="A: ", font=("Courier", 18))
        a_label.place(x = 25, y = 325)

        a_variable = StringVar(self)
        a_variable.set("") # default value
        a_options = OptionMenu(self, a_variable, "", "=", "<", ">")
        a_options.place(x = 160, y = 330)

        a_input = Text(self, height = 1, width = 5)
        a_input.place(x = 210, y = 330)

        e_label = tk.Label(self, text="E: ", font=("Courier", 18))
        e_label.place(x = 25, y = 355)

        e_variable = StringVar(self)
        e_variable.set("") # default value
        e_options = OptionMenu(self, e_variable, "", "=", "<", ">")
        e_options.place(x = 160, y = 360)

        e_input = Text(self, height = 1, width = 5)
        e_input.place(x = 210, y = 360)

        dp_label = tk.Label(self, text="DP: ", font=("Courier", 18))
        dp_label.place(x = 25, y = 385)

        dp_variable = StringVar(self)
        dp_variable.set("") # default value
        dp_options = OptionMenu(self, dp_variable, "", "=", "<", ">")
        dp_options.place(x = 160, y = 390)

        dp_input = Text(self, height = 1, width = 5)
        dp_input.place(x = 210, y = 390)

        fpct_label = tk.Label(self, text="FPCT: ", font=("Courier", 18))
        fpct_label.place(x = 25, y = 415)

        fpct_variable = StringVar(self)
        fpct_variable.set("") # default value
        fpct_options = OptionMenu(self, fpct_variable, "", "=", "<", ">")
        fpct_options.place(x = 160, y = 420)

        fpct_input = Text(self, height = 1, width = 5)
        fpct_input.place(x = 210, y = 420)

        rf_label = tk.Label(self, text="RF: ", font=("Courier", 18))
        rf_label.place(x = 25, y = 445)

        rf_variable = StringVar(self)
        rf_variable.set("") # default value
        rf_options = OptionMenu(self, rf_variable, "", "=", "<", ">")
        rf_options.place(x = 160, y = 450)

        rf_input = Text(self, height = 1, width = 5)
        rf_input.place(x = 210, y = 450)

        dwar_label = tk.Label(self, text="DWAR: ", font=("Courier", 18))
        dwar_label.place(x = 25, y = 475)

        dwar_variable = StringVar(self)
        dwar_variable.set("") # default value
        dwar_options = OptionMenu(self, dwar_variable, "", "=", "<", ">")
        dwar_options.place(x = 160, y = 480)

        dwar_input = Text(self, height = 1, width = 5)
        dwar_input.place(x = 210, y = 480)

        pb_label = tk.Label(self, text="PB: ", font=("Courier", 18))
        pb_label.place(x = 25, y = 505)

        pb_variable = StringVar(self)
        pb_variable.set("") # default value
        pb_options = OptionMenu(self, pb_variable, "", "=", "<", ">")
        pb_options.place(x = 160, y = 510)

        pb_input = Text(self, height = 1, width = 5)
        pb_input.place(x = 210, y = 510)

        csb_label = tk.Label(self, text="CSB: ", font=("Courier", 18))
        csb_label.place(x = 25, y = 535)

        csb_variable = StringVar(self)
        csb_variable.set("") # default value
        csb_options = OptionMenu(self, csb_variable, "", "=", "<", ">")
        csb_options.place(x = 160, y = 540)

        csb_input = Text(self, height = 1, width = 5)
        csb_input.place(x = 210, y = 540)

        cs_label = tk.Label(self, text="CS: ", font=("Courier", 18))
        cs_label.place(x = 25, y = 565)

        cs_variable = StringVar(self)
        cs_variable.set("") # default value
        cs_options = OptionMenu(self, cs_variable, "", "=", "<", ">")
        cs_options.place(x = 160, y = 570)

        cs_input = Text(self, height = 1, width = 5)
        cs_input.place(x = 210, y = 570)

        cspct_label = tk.Label(self, text="CSPCT: ", font=("Courier", 18))
        cspct_label.place(x = 25, y = 595)

        cspct_variable = StringVar(self)
        cspct_variable.set("") # default value
        cspct_options = OptionMenu(self, cspct_variable, "", "=", "<", ">")
        cspct_options.place(x = 160, y = 600)

        cspct_input = Text(self, height = 1, width = 5)
        cspct_input.place(x = 210, y = 600)

        # Checkboxes
        also_label = tk.Label(self, text="Also include: ", font=("Courier", 18))
        also_label.place(x = 450, y = 280)

        city = Checkbutton(self, text="City", variable = IntVar())
        city.place(x = 450, y = 300)

        nickname = Checkbutton(self, text="Team Name", variable = IntVar())
        nickname.place(x = 450, y = 320)

        league = Checkbutton(self, text="League", variable = IntVar())
        league.place(x = 450, y = 340)

        division = Checkbutton(self, text="Division", variable = IntVar())
        division.place(x = 450, y = 360)

        gm = Checkbutton(self, text="General Manager", variable = IntVar())
        gm.place(x = 450, y = 380)

        man = Checkbutton(self, text="Manger", variable = IntVar())
        man.place(x = 450, y = 400)

        stadium = Checkbutton(self, text="Home Stadium", variable = IntVar())
        stadium.place(x = 450, y = 420)

        cap = Checkbutton(self, text="Stadium Capacity", variable = IntVar())
        cap.place(x = 450, y = 440)

        syear = Checkbutton(self, text="Stadium Year", variable = IntVar())
        syear.place(x = 450, y = 460)

        address = Checkbutton(self, text="Address", variable = IntVar())
        address.place(x = 450, y = 480)

        phone = Checkbutton(self, text="Phone Number", variable = IntVar())
        phone.place(x = 450, y = 500)

        web = Checkbutton(self, text="Website", variable = IntVar())
        web.place(x = 450, y = 520)

        fielding_go_button = tk.Button(self, text="GO!", command=lambda: controller.show_frame(StartPage))
        fielding_go_button.place(x = 620, y = 650)

        main_button = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        main_button.place(x = 280, y = 700)

class PagePirates(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="Pirates current 40 man roster", font=("Courier", 20))
        label1.place(x = 155, y = 0)

        divider1 = tk.Label(self, text="______________________________________", font=("Courier", 30))
        divider1.place(x = 0, y = 200)

        filters_label = tk.Label(self, text="Roster Filters:", font=("Courier", 20))
        filters_label.place(x = 250, y = 240)

        divider2 = tk.Label(self, text="______________________________________", font=("Courier", 30))
        divider2.place(x = 0, y = 440)

        filters_label = tk.Label(self, text="2021 Schedule Filters:", font=("Courier", 20))
        filters_label.place(x = 200, y = 480)

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