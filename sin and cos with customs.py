import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import transforms
plt.rcParams["figure.figsize"] = 4,3
from matplotlib.animation import FuncAnimation

r = 10 # radius
def circle(phi):
    return np.array([r*np.cos(phi), r*np.sin(phi)])


# create a figure with an axes
fig, ax = plt.subplots()
# set axes limits
ax.axis([-(r+.5),r+.5,-(r+.5),r+.5])
# set aspect ratio so circle is actually circle
ax.set_aspect("equal")
# create points in the axes
point, = ax.plot(0,0, marker="o")
point2, = ax.plot(0,0, marker="o")
point3, = ax.plot(0,0, marker="o")
point4, = ax.plot(0,0, marker="o")
point5, = ax.plot(0,0, marker="o")


deg = 150
base = plt.gca().transData
rot = transforms.Affine2D().rotate_deg(deg-120)
rot2 = transforms.Affine2D().rotate_deg(deg)
rot3 = transforms.Affine2D().rotate_deg(deg+(deg*2))
rottest = transforms.Affine2D().rotate_deg(120)
rottest2 = transforms.Affine2D().rotate_deg(60)
line, = ax.plot([10,-10], [0,0],'r--')
line2, = ax.plot([10,-10], [0,0],'r--', transform = rot + base )
line3, = ax.plot([10,-10], [0,0],'r--', transform = rot2 + base )
line4, = ax.plot([10,-10], [0,0],'r--', transform = rot3 + base )
point4, = ax.plot(0,0, marker="o", transform = rottest + base)
point5, = ax.plot(0,0, marker="o",transform = rottest2 + base)

def update(phi): 
    x,y = circle(phi)
    Angle = math.degrees(math.atan2(y,x))
    if Angle < 0:
        DegreesAngle = Angle + 360
        print(int(DegreesAngle))
    else:
        print(int(Angle))

    line.set_data([20,-20],[y,y])
    line2.set_data([20,-20],[0,0])
    line3.set_data([20,-20],[0,0])
    line4.set_data([20,-20],[0,0])
    point.set_data([0],[y])
    # point2.set_data([x],[0])
    point3.set_data([x],[y])
    point4.set_data([0],[-x])
    point5.set_data([0],[-x])

    
    return point, point2, point3, point4, point5, line, line2, line3, line4

# create animation with 10ms interval, which is repeated,
# provide the full circle (0,2pi) as parameters
ani = FuncAnimation(fig, update, interval=10, blit=False, repeat=True, frames=np.linspace(0,2*np.pi,360, endpoint=False))
plt.show()