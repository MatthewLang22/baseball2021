import sqlite3
import pandas as pd
filename="script"
con=sqlite3.connect("baseball"+".db")
wb=pd.ExcelFile("project-data"+'.xlsx')
for sheet in wb.sheet_names:
        df=pd.read_excel("project-data"+'.xlsx',sheet_name=sheet)
        df.to_sql(sheet,con, index=False,if_exists="replace")
con.commit()
con.close()