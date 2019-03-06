import matplotlib.pyplot as plt
import numpy as np
import random

#car_passing = [30, 50, 35] 

car_passing = [random.randint(20,60) for i in range(3)]
labels = ['Small', 'Medium', 'Large'] 
colors = ['cyan', '#66b3ff', 'magenta']

index_number_of_highest_val = car_passing.index(max(car_passing))
# fig, ax = plt.subplots()
# ax.pie(car_passing,labels=labels,colors=colors,autopct='%1.1f%%',startangle=90 )

explode = [0 if i!=index_number_of_highest_val else 0.1 for i in range(len(car_passing))]

plt.pie(car_passing,
        labels=labels,
        colors=colors,
        shadow=True,
        explode=explode,
        autopct='%1.1f%%',
        startangle=90 )


plt.title(" Percentage  car passing")
plt.show()
