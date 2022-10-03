import numpy as np
import matplotlib.pyplot as plt

#Figure size (x,y) in inches. Move Legend if changed drasticly to avoid clipping
fig = plt.figure(1, figsize=(14.5, 6.5))

#number of rows/cols of subplots 
ax = fig.add_subplot(1, 1, 1)
#plt.minorticks_on()
#max num ticks in axis
max_yticks = 15
max_xticks = 10 #irrelevant due to log scale
yloc = plt.MaxNLocator(max_yticks)
xloc = plt.MaxNLocator(max_xticks)
ax.yaxis.set_major_locator(yloc)
ax.xaxis.set_major_locator(xloc)
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', length=6)
ax.tick_params(which='both', width=1)

time = [p for p in range(0,2000)]
time2 = [p for p in range(0,2001,250)]
trace1 = [np.cos(2*np.pi/8*t/250) for t in range(0,2000)]
trace2 = [np.cos(2*np.pi*(1/8-1)*t/250) for t in range(0,2000)]
trace3 = [np.cos(2*np.pi*(1/8-1)*t/250) for t in range(0,2001,250)]


plt.plot(time, trace2, "-", alpha=0.8,label = "Reelt signal")
plt.plot(time, trace1, "-", alpha=0.8,label = "Målt signal")
plt.plot(time2, trace3, "o", alpha=0.8, color="black" ,label = "Målepunkt")



plt.grid()
#labels  
plt.xlabel("tid [ms]")
plt.ylabel("Amplitude [V]")
plt.legend(bbox_to_anchor=(0.5, -0.15), loc="upper center",fancybox=True, ncol=8, borderaxespad=0)
plt.tight_layout(rect=[0,0,1,0.98])
plt.show()
plt.rcParams.update({'font.size': 16})

