from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import math
import random

# This function calculates the 3D distance between two points: P1=[x1, y1, z1], P2=[x2, y2, z2]
def distance_two_points(P1_xyz, P2_xyz):
    X_dis = (P2_xyz[0] - P1_xyz[0])**2
    Y_dis = (P2_xyz[1] - P1_xyz[1])**2
    Z_dis = (P2_xyz[2] - P1_xyz[2])**2
    distance = math.sqrt(X_dis + Y_dis + Z_dis)
    return distance

# This draws a sphere
phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2 * np.pi, 40)
x = np.outer(np.sin(theta), np.cos(phi))
y = np.outer(np.sin(theta), np.sin(phi))
z = np.outer(np.cos(theta), np.ones_like(phi))


space = [-1, 1]
points = 1000

x_list = []
y_list = []
z_list = []

x_list_discard = []
y_list_discard = []
z_list_discard = []

for i in range(points):
    X = random.uniform(-1, 1)
    Y = random.uniform(-1, 1)
    Z = random.uniform(-1, 1)        # (0,1) generates points only in the Northern Hemisphere

    Vector = (math.sqrt((X**2) + (Y**2) + (Z**2)))
    X = X / Vector
    Y = Y / Vector
    Z = Z / Vector

    ADD = True
    for i in range(len(x_list)):
        Distance = distance_two_points([X, Y, Z], [x_list[i], y_list[i], z_list[i]])
        #print("point1 =", X, Y, Z)
        #print("point2 =", x_list[i], y_list[i], z_list[i])
        #print(i, Distance)
        #print()
        if Distance < 0.15:
            ADD = False
            break
    if ADD:
        x_list.append(X)
        y_list.append(Y)
        z_list.append(Z)
    else:
        x_list_discard.append(X)
        y_list_discard.append(Y)
        z_list_discard.append(Z)

#for i in range(len(x_list)):
#    print(i, x_list[i], y_list[i], z_list[i])
print(len(x_list))

fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d', 'aspect':'auto'}, figsize=(14, 14))
ax.plot_wireframe(x, y, z, color='k', rstride=1, cstride=1)
ax.scatter(x_list, y_list, z_list, s=20, c='r', zorder=10)
#ax.scatter(x_list_discard, y_list_discard, z_list_discard, s=20, c='b', zorder=10)
plt.savefig("media/Sphere_distance_points_" + str(points) + "_real_" + str(len(x_list)) + ".png", format='png', dpi=150)
plt.show()


def rotate(angle):
    ax.view_init(azim=angle)

rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)
rot_animation.save("media_gif/Sphere_distance_points_" + str(points) + "_real_" + str(len(x_list)) + ".gif", dpi=150, writer="imagemagick")