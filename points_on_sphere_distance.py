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

def generate_distanced_points_on_sphere(points=500, DISTANCE=0.15, debug=False):
    # We store the coordinates of the points in these lists
    x_list = []
    y_list = []
    z_list = []
    # Some points are discarded because they are too close to other points
    x_list_discard = []
    y_list_discard = []
    z_list_discard = []

    for i in range(points):
        # Pick random points
        X = random.uniform(-1, 1)
        Y = random.uniform(-1, 1)
        Z = random.uniform(-1, 1)  # (0,1) generates points only in the Northern Hemisphere

        # This makes sure the points are on the surface of the sphere
        Vector = (math.sqrt((X ** 2) + (Y ** 2) + (Z ** 2)))
        X = X / Vector
        Y = Y / Vector
        Z = Z / Vector

        ADD = True
        for i in range(len(x_list)):
            # This function calculates the 3D distance between two points: P1=[x1, y1, z1], P2=[x2, y2, z2]
            Distance = distance_two_points([X, Y, Z], [x_list[i], y_list[i], z_list[i]])
            if debug:
                print("point1 =", X, Y, Z)
                print("point2 =", x_list[i], y_list[i], z_list[i])
                print(i, Distance)
                print()
            # If the Distance is smaller than decided the points are too close and they are discarded
            if Distance < DISTANCE:
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

    if debug:
        for i in range(len(x_list)):
            print(i, x_list[i], y_list[i], z_list[i])
    print("points on the sphere =", len(x_list))

    return x_list, y_list, z_list, x_list_discard, y_list_discard, z_list_discard

def Points_on_sphere_with_distance(points=500, DISTANCE=0.15, Discarded=False, wireframe=True, plot_surface=False, Show=True, GIF=True, debug=False):
    # This draws the wireframe of a sphere
    phi = np.linspace(0, np.pi, 20)
    theta = np.linspace(0, 2 * np.pi, 40)
    x = np.outer(np.sin(theta), np.cos(phi))
    y = np.outer(np.sin(theta), np.sin(phi))
    z = np.outer(np.cos(theta), np.ones_like(phi))

    # We store the coordinates of the points in these lists
    # Some points are discarded because they are too close to other points
    x_list, y_list, z_list, x_list_discard, y_list_discard, z_list_discard = generate_distanced_points_on_sphere(points=points, DISTANCE=DISTANCE, debug=debug)

    # Use these other points if you want to plot several set of points
    #x_list2, y_list2, z_list2, x_list_discard, y_list_discard, z_list_discard = generate_distanced_points_on_sphere(points=points, DISTANCE=0.35, debug=debug)
    #x_list3, y_list3, z_list3, x_list_discard, y_list_discard, z_list_discard = generate_distanced_points_on_sphere(points=points, DISTANCE=0.55, debug=debug)

    # Plot the data
    fig, ax = plt.subplots(1, 1, subplot_kw={'projection': '3d', 'aspect': 'auto'}, figsize=(14, 14))
    # Plot the wireframe of the sphere
    if wireframe:
        ax.plot_wireframe(x, y, z, color='k', rstride=1, cstride=1, alpha=0.8, linewidth=0.8)
    if plot_surface:
        ax.plot_surface(x, y, z, color='white', rstride=1, cstride=1, alpha=0.4, linewidth=0.8) #shade=False
    # Plot the points
    ax.scatter(x_list, y_list, z_list, s=50, c='r', zorder=10)
    # Plot the discarded points with a different colour
    if Discarded:
        ax.scatter(x_list_discard, y_list_discard, z_list_discard, s=5, c='b', zorder=10)

    # If you want to remove the axis
    #ax.set_axis_off()

    # Create a random seed to save the image
    random_seed = str(random.random())[2:6]

    # Save plot
    plt.savefig("media/Sphere_distance_points_" + str(points) + "_real_" + str(len(x_list)) + "_s" + random_seed + ".png", format='png', dpi=150)
    if Show:
        plt.show()

    def rotate(angle):
        ax.view_init(azim=angle)
    if GIF:
        # rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)     # Smooth and slow, but it is 70MB
        rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 5), interval=200)  # Fast, it is 30MB
        rot_animation.save("media_gif/Sphere_distance_points_" + str(points) + "_real_" + str(len(x_list)) + "_s" + random_seed + ".gif", dpi=150, writer="imagemagick")
    plt.close()
    return None

# test the code
if __name__ == "__main__":
    Points_on_sphere_with_distance(points=3000, DISTANCE=0.25, Discarded=False, wireframe=True, plot_surface=False, Show=True, GIF=True, debug=False)
