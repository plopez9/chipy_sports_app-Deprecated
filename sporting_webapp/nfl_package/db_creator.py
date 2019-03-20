import requests
import pandas as pd
from bs4 import BeautifulSoup
import io


class ImportFootball:
    def __init__(self, year, week):
        self.year = year
        self.week = week
        self.url = "http://rotoguru1.com/cgi-bin/fyday.pl?week=WK&year=YR&game=dk&scsv=1"

    def get_offense (self):
        #Format URL
        url = self.url.replace("YR", str(self.year))
        url = self.url.replace("WK", str(self.week))

        #scrape website
        sauce = requests.get(url).text
        soup = BeautifulSoup(sauce, "html.parser").find_all("pre")
#        soup = io.StringIO(soup)

        #create DataFrame
#        offense_df = pd.read_csv((soup), sep=";")

        return soup

print(ImportFootball(2018, 17).get_offense())
