import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

fig = plt.figure()
ax1= fig.add_subplot(1,1,1)



# def on_press(event):
#     if event.inaxes != ax1: return
#     ax1.press = event.xdata

# def on_release(event):
#     if event.inaxes != ax1: return
#     ax1.press = None
#     ax1.relim()
#     ax1.autoscale_view()

# def on_motion(event):
#     if ax1.press is None:
#         ax1.press = event.xdata
#     if event.inaxes != ax1: return
#     xlim = ax1.get_xlim()
#     dx = event.xdata - ax1.press
#     ax1.set_xlim(xlim[0]+dx, xlim[1]+dx)
#     fig.canvas.draw()
#     ax1.press = event.xdata

# cidpress = fig.canvas.mpl_connect('button_press_event', on_press)
# cidrelease = fig.canvas.mpl_connect('button_release_event', on_release)
# cidmotion = fig.canvas.mpl_connect('motion_notify_event', on_motion)
def animate(i):
    gdata = open('data.txt','r').read()
    lines = gdata.split('\n')
    xs = []
    ys = []
    ts = []
    for line in lines:
        if len(line) > 1:
            try:
                x,y,t = line.split(',')

                xs.append(int(x))
                ys.append(int(y))
                ts.append(t)
            except:
                pass
    # print(ys)
    # print(xs)
    ax1.clear()
    ax1.plot(ts,xs, label= 'temperature')
    ax1.plot(ts,ys, label = 'humidity')
    ax1.set_xlabel("TIME")
    ax1.set_title("FARM MONITORING PROJECT")

    ax1.set_xticks([])
    ax1.legend()

ani = animation.FuncAnimation(fig,animate,interval = 1000)
plt.show()