from StatisticsManager import StatisticsManager
class StatisticsOrchestrator:
    def __init__(self):
        self.manager = StatisticsManager()
    def update():
        try:
            self.manager.update()
        except Exception as ex:
            print(ex)
