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
        label = tk.Label(self, text="Batting!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        button1.pack()




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Pitching!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Fielding!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Pirates!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        

app = SeaofBTCapp()
app.mainloop()