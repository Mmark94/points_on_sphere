import math
from matplotlib import pyplot as plt
from matplotlib import animation
import mpl_toolkits.mplot3d.axes3d as axes3d
import numpy as np
import random


# The fibonacci_sphere function is from from https://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere
def fibonacci_sphere(samples=1000):

    points = []
    phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = math.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        points.append((x, y, z))

    return points

# Plot the points on a sphere
def plot_fibonacci_sphere(samples=1000, wireframe=True, plot_surface=False, Axis=True, Show=True, GIF=True):
    # This draws the wireframe of a sphere
    phi = np.linspace(0, np.pi, 20)
    theta = np.linspace(0, 2 * np.pi, 40)
    x = np.outer(np.sin(theta), np.cos(phi))
    y = np.outer(np.sin(theta), np.sin(phi))
    z = np.outer(np.cos(theta), np.ones_like(phi))

    # Find the points
    points = fibonacci_sphere(samples=samples)
    x_list = [point[0] for point in points]
    y_list = [point[1] for point in points]
    z_list = [point[2] for point in points]
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

    plt.savefig("media_f/Sphere_points_" + str(samples) + "_s" + random_seed + ".png", format='png', dpi=150)
    if Show:
        plt.show()

    def rotate(angle):
        ax.view_init(azim=angle)

    if GIF:
        # rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)     # Smooth and slow, but it is 70MB
        rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 5), interval=200)  # Fast, it is 30MB
        rot_animation.save("media_f_gif/Sphere_points_" + str(samples) + "_s" + random_seed + ".gif", dpi=150, writer="imagemagick")
    plt.close()

# test the code
if __name__ == "__main__":

    #plot_fibonacci_sphere(samples=1000, wireframe=True, plot_surface=False, Axis=True, Show=True, GIF=False)
    #plot_fibonacci_sphere(samples=1000, wireframe=False, plot_surface=False, Axis=True, Show=True, GIF=True)
    plot_fibonacci_sphere(samples=1000, wireframe=False, plot_surface=False, Axis=False, Show=True, GIF=True)
