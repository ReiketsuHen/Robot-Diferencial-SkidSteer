from draw_diff_2by2 import skidsteer
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Pose inicial
x0 = 0
y0 = 0
th0 = 0
pos = np.array([x0, y0, th0])
# Pose deseada
xd = 3
yd = 3
# Contantes fisicas del robot
R = 0.1         # Radio de llantas
L = 0.25        # Long. mayor, llantas-centro
l = 0.2         # Long. menor, llantas-centro
Kv = 0.3
Kw = 1.8

SimTime = 10
dt = 0.01
t = np.arange(0, SimTime+dt, dt)
Pos_t = np.zeros((3, len(t)))
dPos_t = np.zeros((3, len(t)))
WLR_t = np.zeros((2, len(t)))

# Figure
#print(pos)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(autoscale_on=False, xlim=(-4+x0, 4+x0), ylim=(-4+y0, 4+y0))
ax.grid()

#skidsteer(pos, L, l, ax)
#plt.show()

for i in range(0, len(t)-1):
    ev = np.sqrt((xd - pos[0]) ** 2 + (yd - pos[1]) ** 2)
    ew = np.arctan2((yd - pos[1]), (xd - pos[0])) - pos[2]
    ew = np.arctan2(np.sin(ew), np.cos(ew))

    v = Kv * ev
    w = Kw * ew

    Wl = (v + w * l / 4) / R
    Wr = (v - w * l / 4) / R
    dPos = np.array([(R / 2) * (Wl + Wr) * np.cos(pos[2]),
                    (R / 2) * (Wl + Wr) * np.sin(pos[2]),
                    (2 * R / l) * (Wl - Wr)])

    Pos_t[:, i] = pos.T
    dPos_t[:, i] = dPos.T
    #print(Pos_t[:, i])
    #print(t[i])

    pos = pos + dPos*dt

#line, = ax.plot(Pos_t[0, :], Pos_t[1, :])

def animate(i):
    plt.cla()
    plt.title(round(t[i], 4))
    skidsteer(Pos_t[:, i], L, l, ax)
    #return line,

ani = FuncAnimation(fig, animate, frames=np.arange(0, len(t), 2), interval=20)
plt.show()
