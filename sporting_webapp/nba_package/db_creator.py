import requests
import pandas as pd

from bs4 import BeautifulSoup

#Used to create game statistics later
def normalize(series1, series2):
    return (series1/series2)

#scrapes tables from basketball reference
class year_df:
    def __init__(self, year):
        self.year = year

    def url(self):
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

        print(data)

year_df(2018).url()
