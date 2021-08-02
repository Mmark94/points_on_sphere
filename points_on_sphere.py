from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import math
import random

# This draws a sphere
phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2 * np.pi, 40)
x = np.outer(np.sin(theta), np.cos(phi))
y = np.outer(np.sin(theta), np.sin(phi))
z = np.outer(np.cos(theta), np.ones_like(phi))


space = [-1, 1]
points = 100

x_list = []
y_list = []
z_list = []
for i in range(points):
    X = random.uniform(-1, 1)
    Y = random.uniform(-1, 1)
    Z = random.uniform(-1, 1)        # (0,1) generates points only in the Northern Hemisphere
    Vector = (math.sqrt((X**2) + (Y**2) + (Z**2)))
    x_list.append(X/Vector)
    y_list.append(Y/Vector)
    z_list.append(Z/Vector)


fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d', 'aspect':'auto'}, figsize=(14, 14))
ax.plot_wireframe(x, y, z, color='k', rstride=1, cstride=1)
ax.scatter(x_list, y_list, z_list, s=25, c='r', zorder=10)
plt.savefig("media/Sphere_points_" + str(points) + ".png", format='png', dpi=150)
plt.show()

def rotate(angle):
    ax.view_init(azim=angle)

rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)
rot_animation.save("media_gif/Sphere_points_" + str(points) + ".gif", dpi=150, writer="imagemagick")
