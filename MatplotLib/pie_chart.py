import matplotlib.pyplot as plt
import numpy as np


car_passing = [30, 50, 35] 
labels = ['Small', 'Medium', 'Large'] 
colors = ['cyan', '#66b3ff', 'magenta']

# fig, ax = plt.subplots()
# ax.pie(car_passing,labels=labels,colors=colors,autopct='%1.1f%%',startangle=90 )

plt.pie(car_passing,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90 )


plt.title(" Percentage  car passing")
plt.show()
