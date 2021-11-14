import pandas as pd
from Config import Config
from Statistics import Statistics
from StatisticsFileValidator import StatisticsFileValidator
import os
import sys

class StatisticsFileHandler:
    def __init__(self):
        self.dataframe = self.load()
        self.statistics = self.get()

    def get(self):
        statisticsList = []
        for index, row in self.dataframe.iterrows():
            statistics = Statistics(row["date"], row["inflation"], row["interest"], row["growth"], row["unemployment"], row["poverty"])
            statisticsList.append(statistics)
        self.statistics = statisticsList
        return statisticsList

    def doesExist(self):
        return os.path.isfile(Config.STATS.value)

    def __getEmptyDataframe(self):
        return pd.DataFrame(columns=["date", "inflation", "interesting", "growth", "unemployment"])

    def load(self):
        
        if(not self.doesExist()):
            return self.__getEmptyDataframe()

        df = pd.read_csv(Config.STATS.value, sep=";")

        if(not StatisticsFileValidator.validate(df)):
            sys.exit()
        return df 

    def refresh(self):
        self.dataframe = self.load()
        self.statistics = self.get()

    def save(self, newDf):
        pd.read_csv(Config.STATS.value, sep=';').append(newDf).dropna().drop_duplicates(subset=newDf.columns.difference(['date'])).to_csv(Config.STATS.value, sep=';', index=False)
        #newDf.to_csv(Config.STATS.value, mode='a', header=False, sep=';', index=False)
