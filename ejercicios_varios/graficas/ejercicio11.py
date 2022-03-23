"""_summary_

    Using MatPlotLib library to plot graphs

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(" ")
print("Histogramas".center(50, "-"))
print(" ")

datos_uno: np.ndarray = np.random.randn(1000)
print(f"{datos_uno = }")
plt.hist(datos_uno)
plt.show()

