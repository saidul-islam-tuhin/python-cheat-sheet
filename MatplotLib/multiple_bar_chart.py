import matplotlib.pyplot as plt
import numpy as np


n_groups = 3
small_car = (80, 55, 40,)
medium_car = (85, 45, 54)
large_car = (70, 60, 80)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8

for pos,x,y,z in zip(index,small_car,medium_car,large_car):
    ax.text(pos-0.1, x + 2, str(x), color='gray', va='center', fontweight='bold')
    ax.text((pos+bar_width)-0.1, y + 2, str(y), color='gray', va='center', fontweight='bold')
    ax.text((pos+2*bar_width)-0.1, z + 2, str(z), color='gray', va='center', fontweight='bold')
 
small_rect = plt.bar(index, small_car, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Small')
 
medium_rect = plt.bar(index + bar_width, medium_car, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Medium')
 
large_rect = plt.bar(index + 2*bar_width, large_car, bar_width,
                 alpha=opacity,
                 color='c',
                 label='Large')
plt.xlabel('Interarrivale Time')
plt.ylabel('Car')
plt.title('Car passing')
plt.xticks(index + bar_width, ('6AM-1PM', '1PM-9PM', '9PM-6AM',))
plt.legend()
 
plt.tight_layout()
plt.show()