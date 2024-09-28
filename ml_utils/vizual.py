import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def vizualization(x:np.array, x_label:str, y:np.array, y_label:str, title:str):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()