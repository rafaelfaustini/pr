from Statistics import Statistics
from StatisticsFileHandler import StatisticsFileHandler
from StatisticsLoader import StatisticsLoader
class StatisticsManager:
    def __init__(self):
        self.statisticsHandler = StatisticsFileHandler()
        self.statisticsHistory = self.statisticsHandler.statistics

        self.statisticsLoader = StatisticsLoader()
        self.currentStatistics = self.statisticsLoader.loadFromMemory()

    def getLatestStatisticsFromHistory(self):
        self.statisticsHandler.load()
        self.statisticsHistory = self.statisticsHandler.statistics
        return self.statisticsHistory[-1]


    def getCurrentStatisticsFromMemory(self):
        self.currentStatistics = self.statisticsLoader.loadFromMemory()
        return self.currentStatistics

    def refresh(self):
        self.statisticsHandler.refresh()
        self.statisticsLoader.loadFromMemory()

        
    def isUpdated(self):
        historyLatest = self.getLatestStatisticsFromHistory()
        self.getCurrentStatisticsFromMemory()
        return historyLatest == self.currentStatistics

    def update(self):
        if(not self.isUpdated()):
            print("Data updated")

            newStatisticDf = Statistics.toDataframe(self.currentStatistics) 
            historyDf = self.statisticsHandler.dataframe

            history = historyDf.append(newStatisticDf, ignore_index=True)

            self.statisticsHandler.dataframe = history

            self.statisticsHandler.save(newStatisticDf)

            self.refresh()