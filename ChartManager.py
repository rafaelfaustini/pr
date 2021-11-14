from Chart import Chart

class ChartManager:
    @classmethod
    def hook(func):
        ani = FuncAnimation(plt.gcf(), func, interval=5000)

    @classmethod
    def _getLabel(text):
        return text.upper()
    @classmethod
    def _getTitle(x , y):
        return "{x_label} x {y_label}".format(x_label = x.upper(), y_label = y.upper())
    @classmethod
    def plot(x, y, data):
        Chart.plot(ChartManager._getTitle(x, y), ChartManager._getLabel(x), ChartManager._getLabel(y), data)