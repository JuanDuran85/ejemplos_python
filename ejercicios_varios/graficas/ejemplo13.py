"""_summary_

   Multiple plots with Matplotlib and numpy

"""

import matplotlib.pyplot as plt
import numpy as np

def multiple_plots() -> None:
    x: np.ndarray = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)
    
    fig, axs = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    axs[0].plot(x,y)
    axs[1].plot(x,-y)
    plt.show()
    
if __name__ == '__main__':
    multiple_plots()