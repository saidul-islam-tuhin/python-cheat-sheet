import matplotlib.pyplot as plt
import numpy as np


car_passing = [30, 50, 35, 125] # y-axis
car_type = ['Small', 'Medium', 'Large', 'All types car'] # x-axis

fig, ax = plt.subplots()

for x, y in enumerate(car_passing):
    ax.text(x-0.1, y + 3, str(y), color='gray', va='center', fontweight='bold')

ax.bar(car_type, car_passing, color="c")

plt.xlabel(" Car ")
plt.ylabel(" Number of car passing")
plt.title(" How many car passing", color='gray', fontweight='bold')
plt.show()
