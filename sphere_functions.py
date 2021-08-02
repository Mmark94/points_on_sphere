import numpy as np
import math

# sample_spherical is a function to randomly pick points on a sphere
def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

#xi, yi, zi = sample_spherical(100)
#print(xi, yi, zi)

# This function calculates the 3D distance between two points: P1=[x1, y1, z1], P2=[x2, y2, z2]
def distance_two_points(P1_xyz, P2_xyz):
    X_dis = (P2_xyz[0] - P1_xyz[0])**2
    Y_dis = (P2_xyz[1] - P1_xyz[1])**2
    Z_dis = (P2_xyz[2] - P1_xyz[2])**2
    distance = math.sqrt(X_dis + Y_dis + Z_dis)
    return distance
