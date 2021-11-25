# Matthew Lang and Alex Heffner
# 11-24-2021
# CS 4620 Final Project

import sqlite3
import tkinter as tk
from tkinter import *


LARGE_FONT= ("Verdana", 12)

connection = sqlite3.connect("baseball.db")
cursor = connection.cursor()

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

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):

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

        Button(self, text = 'Click Me !', image = batting_pic, command=lambda:[controller.show_frame(PageOne), hitting_query()]).pack()

        blank1 = tk.Label(self, text = "")
        blank1.config(font =("Courier", 30))
        blank1.pack()

        Button(self, text = 'Click Me !', image = pitching_pic, command=lambda:[controller.show_frame(PageTwo), pitching_query()]).pack()

        blank1 = tk.Label(self, text = "")
        blank1.config(font =("Courier", 30))
        blank1.pack()

        Button(self, text = 'Click Me !', image = fielding_pic, command=lambda:[controller.show_frame(PageThree), fielding_query()]).pack()

        blank1 = tk.Label(self, text = "")
        blank1.config(font =("Courier", 30))
        blank1.pack()

        Button(self, text = 'Click Me !', image = pirates_pic, command=lambda:[controller.show_frame(PageFour), pirates_query()]).pack()

        blank1 = tk.Label(self, text = "")
        blank1.config(font =("Courier", 30))
        blank1.pack()

        Button(self, text = 'Click Me !', image = exit_pic, command = self.destroy).pack()


class PageOne(tk.Frame):

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

        gp_label = tk.Label(self, text="GP: ", font=("Courier", 18))
        gp_label.place(x = 25, y = 175)

        gp_variable = StringVar(self)
        gp_variable.set("") # default value
        gp_options = OptionMenu(self, gp_variable, "", "=", "<", ">")
        gp_options.place(x = 160, y = 180)

        gp_input = Text(self, height = 1, width = 5)
        gp_input.place(x = 210, y = 180)

        avg_label = tk.Label(self, text="AVG: ", font=("Courier", 18))
        avg_label.place(x = 25, y = 205)

        avg_variable = StringVar(self)
        avg_variable.set("") # default value
        avg_options = OptionMenu(self, avg_variable, "", "=", "<", ">")
        avg_options.place(x = 160, y = 210)

        avg_input = Text(self, height = 1, width = 5)
        avg_input.place(x = 210, y = 210)

        ab_label = tk.Label(self, text="AB: ", font=("Courier", 18))
        ab_label.place(x = 25, y = 235)

        ab_variable = StringVar(self)
        ab_variable.set("") # default value
        ab_options = OptionMenu(self, ab_variable, "", "=", "<", ">")
        ab_options.place(x = 160, y = 240)

        ab_input = Text(self, height = 1, width = 5)
        ab_input.place(x = 210, y = 240)

        r_label = tk.Label(self, text="R: ", font=("Courier", 18))
        r_label.place(x = 25, y = 265)

        r_variable = StringVar(self)
        r_variable.set("") # default value
        r_options = OptionMenu(self, r_variable, "", "=", "<", ">")
        r_options.place(x = 160, y = 270)

        r_input = Text(self, height = 1, width = 5)
        r_input.place(x = 210, y = 270)

        h_label = tk.Label(self, text="H: ", font=("Courier", 18))
        h_label.place(x = 25, y = 295)

        h_variable = StringVar(self)
        h_variable.set("") # default value
        h_options = OptionMenu(self, h_variable, "", "=", "<", ">")
        h_options.place(x = 160, y = 300)

        h_input = Text(self, height = 1, width = 5)
        h_input.place(x = 210, y = 300)

        b2_label = tk.Label(self, text="2B: ", font=("Courier", 18))
        b2_label.place(x = 25, y = 325)

        b2_variable = StringVar(self)
        b2_variable.set("") # default value
        b2_options = OptionMenu(self, b2_variable, "", "=", "<", ">")
        b2_options.place(x = 160, y = 330)

        b2_input = Text(self, height = 1, width = 5)
        b2_input.place(x = 210, y = 330)

        b3_label = tk.Label(self, text="3B: ", font=("Courier", 18))
        b3_label.place(x = 25, y = 355)

        b3_variable = StringVar(self)
        b3_variable.set("") # default value
        b3_options = OptionMenu(self, b3_variable, "", "=", "<", ">")
        b3_options.place(x = 160, y = 360)

        b3_input = Text(self, height = 1, width = 5)
        b3_input.place(x = 210, y = 360)

        hr_label = tk.Label(self, text="HR: ", font=("Courier", 18))
        hr_label.place(x = 25, y = 385)

        hr_variable = StringVar(self)
        hr_variable.set("") # default value
        hr_options = OptionMenu(self, hr_variable, "", "=", "<", ">")
        hr_options.place(x = 160, y = 390)

        hr_input = Text(self, height = 1, width = 5)
        hr_input.place(x = 210, y = 390)

        rbi_label = tk.Label(self, text="RBI: ", font=("Courier", 18))
        rbi_label.place(x = 25, y = 415)

        rbi_variable = StringVar(self)
        rbi_variable.set("") # default value
        rbi_options = OptionMenu(self, rbi_variable, "", "=", "<", ">")
        rbi_options.place(x = 160, y = 420)

        rbi_input = Text(self, height = 1, width = 5)
        rbi_input.place(x = 210, y = 420)

        sb_label = tk.Label(self, text="SB: ", font=("Courier", 18))
        sb_label.place(x = 25, y = 445)

        sb_variable = StringVar(self)
        sb_variable.set("") # default value
        sb_options = OptionMenu(self, sb_variable, "", "=", "<", ">")
        sb_options.place(x = 160, y = 450)

        sb_input = Text(self, height = 1, width = 5)
        sb_input.place(x = 210, y = 450)

        cs_label = tk.Label(self, text="CS: ", font=("Courier", 18))
        cs_label.place(x = 25, y = 475)

        cs_variable = StringVar(self)
        cs_variable.set("") # default value
        cs_options = OptionMenu(self, cs_variable, "", "=", "<", ">")
        cs_options.place(x = 160, y = 480)

        cs_input = Text(self, height = 1, width = 5)
        cs_input.place(x = 210, y = 480)

        bb_label = tk.Label(self, text="BB: ", font=("Courier", 18))
        bb_label.place(x = 25, y = 505)

        bb_variable = StringVar(self)
        bb_variable.set("") # default value
        bb_options = OptionMenu(self, bb_variable, "", "=", "<", ">")
        bb_options.place(x = 160, y = 510)

        bb_input = Text(self, height = 1, width = 5)
        bb_input.place(x = 210, y = 510)

        so_label = tk.Label(self, text="SO: ", font=("Courier", 18))
        so_label.place(x = 25, y = 535)

        so_variable = StringVar(self)
        so_variable.set("") # default value
        so_options = OptionMenu(self, so_variable, "", "=", "<", ">")
        so_options.place(x = 160, y = 540)

        so_input = Text(self, height = 1, width = 5)
        so_input.place(x = 210, y = 540)

        obp_label = tk.Label(self, text="OBP: ", font=("Courier", 18))
        obp_label.place(x = 25, y = 565)

        obp_variable = StringVar(self)
        obp_variable.set("") # default value
        obp_options = OptionMenu(self, obp_variable, "", "=", "<", ">")
        obp_options.place(x = 160, y = 570)

        obp_input = Text(self, height = 1, width = 5)
        obp_input.place(x = 210, y = 570)

        slg_label = tk.Label(self, text="SLG: ", font=("Courier", 18))
        slg_label.place(x = 25, y = 595)

        slg_variable = StringVar(self)
        slg_variable.set("") # default value
        slg_options = OptionMenu(self, slg_variable, "", "=", "<", ">")
        slg_options.place(x = 160, y = 600)

        slg_input = Text(self, height = 1, width = 5)
        slg_input.place(x = 210, y = 600)

        ops_label = tk.Label(self, text="OPS: ", font=("Courier", 18))
        ops_label.place(x = 25, y = 625)

        ops_variable = StringVar(self)
        ops_variable.set("") # default value
        ops_options = OptionMenu(self, ops_variable, "", "=", "<", ">")
        ops_options.place(x = 160, y = 630)

        ops_input = Text(self, height = 1, width = 5)
        ops_input.place(x = 210, y = 630)

        batting_go_button = tk.Button(self, text="GO!", command=lambda: controller.show_frame(StartPage))
        batting_go_button.place(x = 620, y = 650)

        main_button = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        main_button.place(x = 280, y = 700)

class PageTwo(tk.Frame):

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

        batting_go_button = tk.Button(self, text="GO!", command=lambda: controller.show_frame(StartPage))
        batting_go_button.place(x = 620, y = 650)

        main_button = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        main_button.place(x = 280, y = 700)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Fielding Filters", font=("Courier", 30))
        label.place(x = 185, y = 0)

        fielding_go_button = tk.Button(self, text="GO!", command=lambda: controller.show_frame(StartPage))
        fielding_go_button.place(x = 620, y = 650)

        main_button = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        main_button.place(x = 280, y = 700)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Pirates!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        

app = SeaofBTCapp()
app.mainloop()