from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from numpy import arange, meshgrid
from matplotlib.cm import *
from FinalTorusVectorField import getTorusXYZ
from FinalSphereVectorField import getSphereXYZ
from FinalKleinVectorField import getBottleXYZ
from ProjectivePlaneVectorField import getBoyXYZ


def plotSurface(func):
    global i
    fig = plt.figure(0)
    ax = fig.gca(projection='3d')

    u = arange(-1, 1.05, 0.05)
    v = arange(0, 4.05, 0.05)

    try:
        u, v = meshgrid(u, v)
        x, y, z = func(u, v, 1)
        ax.plot_surface(x, y, z)
    except TypeError:
        t = arange(-1, 1.005, 0.005)
        u, v = meshgrid(t, t)
        x, y, z = func(u, v)
        ax.plot_surface(x, y, z, alpha=0.5)

    if func == getTorusXYZ:
        ax.view_init(60, -60)
    elif func == getSphereXYZ:
        ax.view_init(25, -25)
    elif func == getBottleXYZ:
        ax.view_init(60, -60)
    else:
        ax.view_init(50, 100)
    plt.savefig("temp/{}.png".format(i))
    i += 1
    plt.show()

i=0
plotSurface(getTorusXYZ)
plotSurface(getSphereXYZ)
plotSurface(getBottleXYZ)
plotSurface(getBoyXYZ)
