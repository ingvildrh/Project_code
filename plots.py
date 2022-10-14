import numpy as np
from MPC_run import *
import matplotlib.pyplot as plt

exe_time = np.matrix(tosave)

time_arr = exe_time
for i in range(tend):
    exe_time[0, i] = i


fig, ax = plt.subplots()
ax.plot(exe_time, time_arr, 'b-', linewidth=2)
ax.set_title('Python Execution time')
ax.set_ylabel('Execution time [micro seconds]')
ax.set_xlabel('Step')

#ylim(min(cars,trucks),max(cars,trucks))
# Create a legend
ax.legend(['time', 'steps'], loc = 'best')

plt.show()