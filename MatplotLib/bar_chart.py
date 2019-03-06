import matplotlib.pyplot as plt
import numpy as np


car_passing = [30, 50, 35, 125] # y-axis
car_type = ['Small', 'Medium', 'Large', 'All types car'] # x-axis

plt.bar(car_type, car_passing)

plt.xlabel(" Car ")
plt.ylabel(" Number of car passing")
plt.title(" How many car passing")
plt.show()
