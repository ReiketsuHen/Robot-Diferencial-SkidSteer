import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#fig = plt.figure(figsize=(8, 6))
#ax = fig.add_subplot(autoscale_on=False, xlim=(-4, 4), ylim=(-4, 4))
#ax.grid()

def skidsteer(pos, L, l, ax):
    x = pos[0]
    y = pos[1]
    theta = pos[2]

    ax.grid()
    ax.set_xlim(-4+0, 4+0)
    ax.set_ylim(-4+0, 4+0)

    Lo = L*0.3
    lo = L*0.2
    Tob = np.array([[np.cos(theta), -np.sin(theta), x],
                    [np.sin(theta), np.cos(theta), y],
                    [0, 0, 1]])
    Tblf = [[1, 0, L], [0, 1, l], [0, 0, 1]]
    Tbrf = [[1, 0, L], [0, 1, -l], [0, 0, 1]]
    Tblb = [[1, 0, -L], [0, 1, l], [0, 0, 1]]
    Tbrb = [[1, 0, -L], [0, 1, -l], [0, 0, 1]]

    Tolf = Tob@Tblf
    Torf = Tob@Tbrf
    Tolb = Tob@Tblb
    Torb = Tob@Tbrb

    #Base
    phi = np.linspace(0, 2*np.pi, 50)
    pc = Tob @ np.array([[L*0.7], [0], [1]])

    cx = pc[0]+L*0.15*np.cos(phi)
    cy = pc[1]+L*0.15*np.sin(phi)
    ax.plot(cx, cy, 'r', linewidth=2, markersize=10)

    p1 = Tob@[[+L+Lo], [-l+lo], [1]]
    p2 = Tob@[[-L-Lo], [-l+lo], [1]]
    p3 = Tob@[[-L-Lo], [+l-lo], [1]]
    p4 = Tob@[[+L+Lo], [+l-lo], [1]]
    plt.plot(np.array([p1[0], p2[0], p3[0], p4[0], p1[0]]), np.array([p1[1], p2[1], p3[1], p4[1], p1[1]]), 'b')

    #Ruedas
    #Delantera Izq
    p1 = Tolf @ [[+Lo], [-lo], [1]]
    p2 = Tolf @ [[-Lo], [-lo], [1]]
    p3 = Tolf @ [[-Lo], [+lo], [1]]
    p4 = Tolf @ [[+Lo], [+lo], [1]]
    plt.plot(np.array([p1[0], p2[0], p3[0], p4[0], p1[0]]), np.array([p1[1], p2[1], p3[1], p4[1], p1[1]]), 'b')

    #Delantera Der
    p1 = Torf @ [[+Lo], [-lo], [1]]
    p2 = Torf @ [[-Lo], [-lo], [1]]
    p3 = Torf @ [[-Lo], [+lo], [1]]
    p4 = Torf @ [[+Lo], [+lo], [1]]
    plt.plot(np.array([p1[0], p2[0], p3[0], p4[0], p1[0]]), np.array([p1[1], p2[1], p3[1], p4[1], p1[1]]), 'b')

    #Trasera  Izq
    p1 = Tolb @ [[+Lo], [-lo], [1]]
    p2 = Tolb @ [[-Lo], [-lo], [1]]
    p3 = Tolb @ [[-Lo], [+lo], [1]]
    p4 = Tolb @ [[+Lo], [+lo], [1]]
    plt.plot(np.array([p1[0], p2[0], p3[0], p4[0], p1[0]]), np.array([p1[1], p2[1], p3[1], p4[1], p1[1]]), 'b')

    #Trasera  Der
    p1 = Torb @ [[+Lo], [-lo], [1]]
    p2 = Torb @ [[-Lo], [-lo], [1]]
    p3 = Torb @ [[-Lo], [+lo], [1]]
    p4 = Torb @ [[+Lo], [+lo], [1]]
    plt.plot(np.array([p1[0], p2[0], p3[0], p4[0], p1[0]]), np.array([p1[1], p2[1], p3[1], p4[1], p1[1]]), 'b')

    #plt.show()

