import matplotlib.pyplot as plt

class Chart:
    @classmethod
    def plot(title, labelX, labelY, x, y):
        plt.cla()
        #plt.tick_params(axis='x', which='major', labelsize=2)
        plt.title(title)
        plt.xlabel(labelX)
        plt.ylabel(labelY)
        plt.plot(pd.to_datetime(x, y))
        plt.tight_layout()