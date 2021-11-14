
from Memory import Memory
from Config import Config
from MemoryAddress import MemoryAddress
from Statistics import Statistics
from datetime import datetime

class StatisticsLoader:

    def __init__(self, inflation=None, interest=None, growth=None, unemployment = None, poverty = None):
        self.memory = Memory()
        self.statistics = Statistics()

    def loadFromMemory(self):
        try:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            inflation = self.get_inflation_rate()
            interest = self.get_interesting_rate()
            growth = self.get_growth_rate()
            unemployment = self.get_unemployment_rate()
            poverty = self.get_poverty_rate()
            return Statistics(date, inflation, interest, growth, unemployment, poverty)
        except Exception as ex:
            print(ex)
            return Statistics()


    def get_inflation_rate(self):
        inflation = self.memory.getFloat(MemoryAddress.INFLATION.value)
        return round(inflation, Config.ROUND_DECIMALS.value)  * 100

    def get_interesting_rate(self):
        interesting = self.memory.getFloat(MemoryAddress.INTEREST.value)
        return round(interesting, Config.ROUND_DECIMALS.value) * 100
   
    def get_growth_rate(self):
        growth = self.memory.getFloat(MemoryAddress.GROWTH.value)
        return round(growth, Config.ROUND_DECIMALS.value) * 100

    def get_unemployment_rate(self):
        unemployment = self.memory.getFloat(MemoryAddress.UNEMPLOYMENT.value)
        return round(unemployment, Config.ROUND_DECIMALS.value) * 100
    
    def get_poverty_rate(self):
        poverty = self.memory.getFloat(MemoryAddress.POVERTY.value)
        return round(poverty, Config.ROUND_DECIMALS.value) * 100