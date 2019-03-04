import requests
import pandas as pd
import sqlite3 as sq

from bs4 import BeautifulSoup
from sqlalchemy import create_engine

#Used to create game statistics later

#def construct_id(series):
#    counter = 0
#    tuple_list = []
#    for item in series[0]:
#        tuple_list = tuple_list+[item[counter], counter]
#        counter = counter + 1
#        return tuple_list

#scrapes tables from basketball reference
class SummaryScrape:
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

        #Clean columns
        data = data.drop(["Pos", "Age", ], axis=1)

        #Create Player IDs
        print(data.head(5))

class TeamScrape:
    def __init__(self, year):
        self.year = year
        self.teams = ['OKC', 'PHO', 'ATL', 'MIA', 'CLE',
        'DEN', 'SAS', 'CHI', 'UTA', 'BRK', 'NYK', 'POR',
        'MEM', 'IND', 'MIL', 'HOU', 'TOR', 'WAS', 'ORL',
        'CHO', 'SAC', 'LAL', 'DAL', 'MIN', 'BOS', 'GSW',
        'LAC', 'PHI', 'DET', 'NOP',]
        self.url = "https://www.basketball-reference.com/teams/TM/yr.html"

    def get_players(self):

        #create empty dataframe
        p_table=pd.DataFrame()

        #Scrape Data
        for item in self.teams:
            #edit url
            url_foo = self.url.replace("yr", str(self.year))
            url_foo = url_foo.replace("TM", item)

            #create the sauce
            sauce = requests.get(url_foo).text
            soup = BeautifulSoup(sauce,"lxml")

            #find column names
            roster_header = [[t.text for t in p.find_all("th")]
            for p in soup.find_all("tr")][0][1:]

            #extract databa
            roster_data = [[t.text for t in p.find_all("td")]
            for p in soup.find_all("tr")][1:]

            #create dataframe
            data = pd.DataFrame(roster_data, columns=roster_header)

            #add url
            player_url =[p.find("a") for p in soup.find_all("tr")][1:]
            player_url =[url.get("href") for url in player_url]
            data["URL"] = player_url

            #add team and year
            data["Year"] = self.year

            #append to DataFrame
            p_table = p_table.append(data)

            #Reset URL
            url_foo =self.url

    def get_offense(self):
        print("test")

    def get_defense(self):
        print(" worked")
#Test Code
TeamScrape(2019).get_offense()
TeamScrape(2019).get_defense()





#===============================================================================
##Make Empty DataFrame
#data = pd.DataFrame()

##Loop through the league since the Current League Construction
#for x in range (2010, 2019):
#    data = data.append(year_df(x).make_data())

##Create Database
#engine = create_engine(r"sqlite:///C:\Users\Pedro\Desktop\Programs\chipy_sports_app\sporting_webapp\nba_package\nba.db")
#data.to_sql("Player Totals", con = engine, if_exists= "replace", chunksize = 10)

#===============================================================================
##Check database/query
#connection = sq.connect("nba.db")
#c = connection.cursor()
#c.execute("SELECT * FROM 'Player Totals' WHERE Player == 'LeBron James'")

#print(c.fetchall())
#connection.close()
