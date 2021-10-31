from matplotlib import pyplot as plt
from matplotlib import animation
import mpl_toolkits.mplot3d.axes3d as axes3d
import numpy as np
import math
import random

def random_points_on_sphere(points=500, wireframe=True, plot_surface=False, Axis=True, Show=True, GIF=True):
    # This draws the wireframe of a sphere
    phi = np.linspace(0, np.pi, 20)
    theta = np.linspace(0, 2 * np.pi, 40)
    x = np.outer(np.sin(theta), np.cos(phi))
    y = np.outer(np.sin(theta), np.sin(phi))
    z = np.outer(np.cos(theta), np.ones_like(phi))

    # We store the coordinates of the points in these lists
    x_list = []
    y_list = []
    z_list = []
    for i in range(points):
        # Pick random points
        X = random.uniform(-1, 1)
        Y = random.uniform(-1, 1)
        Z = random.uniform(-1, 1)  # (0,1) generates points only in the Northern Hemisphere

        # This makes sure the points are on the surface of the sphere
        Vector = (math.sqrt((X ** 2) + (Y ** 2) + (Z ** 2)))
        x_list.append(X / Vector)
        y_list.append(Y / Vector)
        z_list.append(Z / Vector)

    # Plot the data
    fig, ax = plt.subplots(1, 1, subplot_kw={'projection': '3d', 'aspect': 'auto'}, figsize=(14, 14))
    # Plot the wireframe of the sphere
    if wireframe:
        ax.plot_wireframe(x, y, z, color='k', rstride=1, cstride=1, alpha=0.8, linewidth=0.8)
    if plot_surface:
        ax.plot_surface(x, y, z, color='white', rstride=1, cstride=1, alpha=0.4, linewidth=0.8) #shade=False
    # Plot the points
    ax.scatter(x_list, y_list, z_list, s=30, c='r', zorder=10)

    # If you want to remove the axis
    if not(Axis):
        ax.set_axis_off()

    # Create a random seed to save the image
    random_seed = str(random.random())[2:6]

    plt.savefig("media/Sphere_points_" + str(points) + "_s" + random_seed + ".png", format='png', dpi=150)
    if Show:
        plt.show()

    def rotate(angle):
        ax.view_init(azim=angle)

    if GIF:
        # rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)     # Smooth and slow, but it is 70MB
        rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 5), interval=200)  # Fast, it is 30MB
        rot_animation.save("media_gif/Sphere_points_" + str(points) + "_s" + random_seed + ".gif", dpi=150, writer="imagemagick")
    plt.close()
    return None

# test the code
if __name__ == "__main__":

    random_points_on_sphere(points=500, wireframe=True, plot_surface=False, Axis=True, Show=True, GIF=False)
