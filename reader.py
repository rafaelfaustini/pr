from subprocess import check_output
import ctypes
import win32api as wapi
import win32process as wproc
import win32con as wcon

import psutil
import pymem
import pymem.process
import pymem.memory

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
from decimal import Decimal 
import os

import pandas as pd

import math

from Statistics import Statistics

plt.style.use('fivethirtyeight')


class Statistic:

    def __init__(self):
        
        if os.path.isfile("gs_stats.csv"):
            self.df = pd.read_csv("gs_stats.csv", sep=";")
            self.last = {
                "date": self.df["date"].iloc[-1],
                "inflation": self.df["inflation"].iloc[-1],
                "interest": self.df["interest"].iloc[-1],
                "growth": self.df["growth"].iloc[-1],
                "unemployment": self.df["unemployment"].iloc[-1],
                "poverty": self.df["poverty"].iloc[-1]
            }
        else:
            self.last = {
                "date": None,
                "inflation": None,
                "interest": None,
                "growth": None,
                "unemployment": None,
                "poverty": None
            }
            self.df = pd.DataFrame(columns=["date", "inflation", "interest", "growth", "unemployment"])

        self.statistics = Statistics()

        #print(self.df)
        ani = FuncAnimation(plt.gcf(), self.checarStatistics, interval=1000)
        plt.tight_layout()
        plt.show()

    def writeCsv(self):
        #print(self.df)
        self.df = self.df.append(pd.DataFrame({
            "date": [self.last["date"]],
            "inflation": [self.last["inflation"]],
            "interest": [self.last["interest"]],
            "growth": [self.last["growth"]],
            "unemployment": [self.last["unemployment"]],
            "poverty": [self.last["poverty"]]
            }))
        self.df.to_csv("gs_stats.csv", sep=';', index=False)




    def checarStatistics(self, i):
        #print(gps)
        self.statistics.loadFromMemory()

        currentStats = Statistics(self.last["inflation"], self.last["interest"], self.last["growth"], self.last["unemployment"], self.last["poverty"])


        if self.statistics != currentStats:
            #print(self.last)
            #print("Updated")
            self.last["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.last["inflation"] = self.statistics.inflation
            self.last["interest"] = self.statistics.interest
            self.last["growth"] = self.statistics.growth
            self.last["unemployment"] = self.statistics.unemployment
            self.last["poverty"] = self.statistics.poverty
            self.writeCsv()
        self.plot()

    def plot(self):
        plt.cla()
        #plt.tick_params(axis='x', which='major', labelsize=2)
        plt.title('Inflation x Real Time')
        plt.xlabel("real time")
        plt.ylabel("inflation")
        plt.plot(pd.to_datetime(self.df["date"], infer_datetime_format=True).astype('int64'), self.df["inflation"].to_numpy())
        plt.tight_layout()

start = Statistic()




