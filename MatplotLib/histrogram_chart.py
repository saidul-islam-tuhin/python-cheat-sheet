import matplotlib.pyplot as plt
import numpy as np
import random
import datetime
import calendar

today = datetime.date.today()
total_days_in_current_month = calendar.monthrange(today.year, today.month)[1]
month_name = calendar.month_name[today.month]

y_axis_data = [ random.randint(20,60) for i in range(total_days_in_current_month)]
x_axis_data = [ i for i in range(1,total_days_in_current_month+1)]
print(y_axis_data)
fig, ax = plt.subplots()
ax.bar(x_axis_data, y_axis_data, color="c")


plt.xlabel(" Days of {} ".format(month_name))
plt.ylabel(" Number of car passing")
plt.title(" How many car passing", color='gray', fontweight='bold')
plt.show()