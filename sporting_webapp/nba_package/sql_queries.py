import pandas as pd
import sqlite3 as sq

from sqlalchemy import create_engine

#===============================================================================
##Check database/query
engine = create_engine(r"sqlite:///C:\Users\Pedro\Desktop\Programs\chipy_sports_app\sporting_webapp\nba_package\nba.db")
c = engine.connect()
print(c.execute("SELECT * FROM 'Player Info' WHERE Player == 'Jimmy Butler'").fetchall())
print(c.execute("SELECT * FROM 'Summary Stats' WHERE Player == 'Jimmy Butler'").fetchall())
c.close()
