import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data_poly.csv")

X = data["x"]
Y = data["y"]

X = np.array(X)
Y = np.array(Y)

a,b,c = np.polyfit(X,Y, 2)
z = np.arange(100)

plt.scatter(X,Y, color="red")
plt.plot(z, a*z**2+b*z+c, color="blue")
plt.show()