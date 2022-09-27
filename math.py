import numpy as np
import matplotlib.pyplot as plt
zeta1 = 0.92388
zeta2 = 0.38268

fs = 5900
margin = 0.8


w0 = fs*2*np.pi*margin

tau1 = 1/(w0*zeta1)
tau2 = 1/(w0**2*tau1)
tau3 = 1/(w0*zeta2)
tau4 = 1/(w0**2*tau3)

R= 2000

C1 = tau1/R
C2 = tau2/R
C3 = tau3/R
C4 = tau4/R


print(f"C1: {C1}")
print(f"C2: {C2}")




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

time = [p for p in range(1000,10000,30)]
trace1 = [tau1/R*10**9 for R in range(1000,10000,30)]
trace2 = [tau2/R*10**9 for R in range(1000,10000,30)]
trace3 = [tau3/R*10**9 for R in range(1000,10000,30)]
trace4 = [tau4/R*10**9 for R in range(1000,10000,30)]

plt.plot(time, trace1, "-", alpha=0.8,label = "C1")
plt.plot(time, trace2, "-", alpha=0.8,label = "C2")
plt.plot(time, trace3, "-", alpha=0.8,label = "C3")
plt.plot(time, trace4, "-", alpha=0.8,label = "C4")


#labels  
plt.xlabel("Impedanse R")
plt.ylabel("nF")
  
  
  
#Final touch
# ellipse = Ellipse(xy=(580, -24), width=900, height=10, 
#                       edgecolor='r', fc='None', lw=2)
# ax.add_patch(ellipse)

#ypoints = [(0,580),(-44,580)]

# #plt.plot(ypoints, linestyle = 'dotted')
# plt.axvline(x=5650, ymin=-0.95, ymax=0.95, linestyle = (0,(5,1)), color = 'tab:orange',label='$f_0 = 5650$ Hz')
# plt.axvline(x=11300, ymin=-0.95, ymax=0.95, linestyle = (0,(5,1)), color = 'tab:green',label='$f_1 = 11300$ Hz')
# plt.axvline(x=16950, ymin=-0.95, ymax=0.95, linestyle = (0,(5,1)), color = 'tab:red',label='$f_2  = 16950$ Hz')
#legend. Source: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib
plt.legend(bbox_to_anchor=(0.5, -0.15), loc="upper center",fancybox=True, ncol=8, borderaxespad=0)
plt.tight_layout(rect=[0,0,1,0.98])
plt.show()