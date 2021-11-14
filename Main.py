import sched  
import datetime, time
from StatisticsManager import StatisticsManager
from PeriodicScheduler import PeriodicScheduler

s = sched.scheduler(time. time, time.sleep)
manager = StatisticsManager()

def draw():
    manager.update()

periodic_scheduler = PeriodicScheduler()  
periodic_scheduler.setup(1, draw)  
periodic_scheduler.run() 