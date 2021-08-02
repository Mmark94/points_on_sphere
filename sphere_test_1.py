import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a sphere
r = 1
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)

#Import data
#data = np.genfromtxt('leb.txt')
data = np.array([[1,0,1],[1,-1,1],[0,0,1]])
theta, phi, r = np.hsplit(data, 3)
theta = theta * pi / 180.0
phi = phi * pi / 180.0
xx = sin(phi)*cos(theta)
yy = sin(phi)*sin(theta)
zz = cos(phi)

#Set colours and render
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    x, y, z,  rstride=1, cstride=1, color='c', alpha=0.3, linewidth=0)

ax.scatter(xx,yy,zz,color="k",s=20)

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("auto")
plt.tight_layout()
plt.show()