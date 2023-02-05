import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

fig = plt.figure()
ax1= fig.add_subplot(1,1,1)
def animate(i):
    gdata = open('data.txt','r').read()
    lines = gdata.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            try:
                x,y = line.split(',')

                xs.append(int(x))
                ys.append(int(y))
            except:
                pass
    # print(ys)
    # print(xs)
    ax1.clear()
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig,animate,interval = 1000)
plt.show()