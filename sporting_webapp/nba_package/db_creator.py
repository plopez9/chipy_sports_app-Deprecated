import requests
import pandas as pd
import sqlite3 as sq

from bs4 import BeautifulSoup
from sqlalchemy import create_engine

#Used to create game statistics later
def normalize(series1, series2):
    return (series1/series2)

#scrapes tables from basketball reference
class year_df:
    def __init__(self, year):
        self.year = year

    def make_data(self):
        #Import soup from basketball reference url
        url_foo = "https://www.basketball-reference.com/leagues/NBA_yr_totals.html"
        sauce = requests.get(url_foo.replace("yr", str(self.year))).text
        soup = BeautifulSoup(sauce, "lxml")

        #extract table content
        db_data = [[data.text for data in record.find_all("td")]
        for record in soup.find_all("tr")]

        #extract table header
        cols = [header.text for header in soup.find("tr").find_all("th")]

        #create data frame
        data = pd.DataFrame(db_data[1:], columns=cols[1:])
        data.dropna(how="all", axis=0, inplace=True)

        #Format strings to numeric
        data.loc[:,"G":] = data.loc[:,"G":].apply(pd.to_numeric)
        data["Age"]=pd.to_numeric(data["Age"])

        #Create Year Column in DataFrame
        data["Year"] = self.year

        return data

#===============================================================================
##Make Empty DataFrame
#data = pd.DataFrame()

##Loop through the league since the Three Point Line
#for x in range (1979, 2019):
#    data = data.append(year_df(x).make_data())

##Create Database
#engine = create_engine(r"sqlite:///C:\Users\Pedro\Desktop\Programs\chipy_sports_app\sporting_webapp\nba_package\nba.db")
#data.to_sql("Player Totals", con = engine, if_exists= "replace", chunksize = 10)

#===============================================================================
##Check database/query
connection = sq.connect("nba.db")
c = connection.cursor()
c.execute("SELECT * FROM 'Player Totals'")

print(c.fetchmany(5))
connection.close()
