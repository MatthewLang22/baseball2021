# **2021 Major League Baseball Statistical Database Program**
### **Created by: Matthew Lang and Alex Heffner**

### **About:**
For our CS 4620 Final Project, we implemented a Major League Baseball database and program. We created our MLB database from scratch - using Python and SQLite3. We filled our database with a lot of baseball related information that is relevant to one individual Major League Baseball team, specifically for this program, the Pittsburgh Pirates. In our database, we implemented 6 different tables. Our database contains tables of batting, pitching, and fielding statistics of all players who played Major League Baseball in 2021. We also have a table containing information on each MLB Organization - such as their ballpark name, address, general manager’s name, and contact information. There is a table for Pittsburgh Pirate players only, containing their personal information, along with links to their 2021 highlights, profile, and walk up songs. Finally, we implemented a table containing the results of all the Pirates 162 individual games for the 2021 season, including the date, opponent, and final score.  
<br />
This program is intended to be used by a MLB organization's front office / data science team. We used Python as our base language to create an application where a user can access and view information in our database by running many customizable queries through a menu. For example, one query that a user might (indirectly) run is, “Select all players who batted over .315 and played over 130 games in the season”. All queries are dynamically based upon user input inside the GUI. 
<br />

### **Installation:**
- **Python** : https://www.python.org/downloads/
- **Tkinter** : Windows: (pip install tkinter) Mac: (pip3 install tkinter)
- **SQLite3** : https://www.sqlite.org/download.html
<br />

Additionally - If on a Windows machine or using wsl:
    Install Xming X server for Windows: 
    https://sourceforge.net/projects/xming/?source=typ_redirect
    add export DISPLAY=:0; to end of .bashrc
    run Xming then run the python code

### **Execution:**
- Clone this repository, and navegate to corresponding folder
- Run command: "python3 main.py"

### **Data credits:**
Batting: https://www.cbssports.com/mlb/stats/player/batting/mlb/regular/all-pos/all/?sortcol=gp&sortdir=descending 

Pitching: https://www.cbssports.com/mlb/stats/player/pitching/mlb/regular/all-pos/all/?sortcol=gp&sortdir=descending 

Fielding: https://www.espn.com/mlb/stats/fielding/_/seasontype/2/sort/gamesPlayed/qualified/false/order/true 

Pirates: https://www.mlb.com/pirates/roster , https://pittsburghbaseballnow.com/pittsburgh-pirates-walkup-songs/ 

Schedule: https://www.baseball-reference.com/teams/PIT/2021-schedule-scores.shtml 

Teams: https://waxpackhero.com/mlb-team-addresses 
