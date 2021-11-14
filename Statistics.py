import pandas as pd
class Statistics:
    def __init__(self, date=None, inflation=None, interest=None, growth=None, unemployment = None, poverty = None):
        self.date = date
        self.inflation = inflation
        self.interest = interest
        self.growth = growth
        self.unemployment = unemployment
        self.poverty = poverty

    def __eq__(self, other): 
        if not isinstance(other, Statistics):
            # don't attempt to compare against unrelated types
            return NotImplemented
        isEqual = True
        for attr in vars(self):
            isEqual = isEqual and (getattr(self, attr) == getattr(other,attr) or attr == "date")
        return isEqual

    def isNull(self):
        isNotNull = self.date and self.inflation and self.interest and self.growth and self.unemployment and self.poverty
        return not isNotNull

    @classmethod
    def toDataframe(cls, obj):
        df = {}
        for attr in vars(obj):
            df[attr] = getattr(obj, attr)
        return pd.DataFrame([df])