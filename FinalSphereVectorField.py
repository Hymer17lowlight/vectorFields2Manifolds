import matplotlib.pyplot as plt
from numpy import sin, cos, pi, arange, meshgrid
from mpl_toolkits.mplot3d import Axes3D
from FinalTorusVectorField import plotAll


def getSphereXYZ(u, v, m):
    u, v = pi*u/m, pi*v/4
    x = 4*cos(u)*sin(v)
    y = 4*sin(u)*sin(v)
    z = 4*cos(v)
    return x, y, z


def getAllS(n, k):
    if n ** 2 + k ** 2 == 0:
        m = 1
    else:
        m = max(n, k)
    u = arange(-m, m + 0.05, 0.05)
    v = arange(0, 4.05, 0.05)
    u, v = meshgrid(u, v)
    du = cos(pi * u * ((n + k) - (n - k) * sin(pi * v / 2)) / (2 * m))
    dv = sin(pi*v/2)
    return u, v, du, dv


if __name__ == '__main__':
    i = 6
    while True:
        try:
            n = int(input('number of inlets: '))-1
            k = int(input('number of outlets: '))-1
            fig, ax, plot = plotAll(getSphereXYZ, n, k, field=getAllS)
            ax.view_init(30, 117)
            plt.savefig("temp/sphere/temps{}.png".format(i))
            plt.show()
            i += 1

            ax.set_axis_off()

            ax.set_facecolor('k')
            plot.set_facecolor('k')
        except IndexError:
            print("It's impossible")
            continue
        except ValueError:
            print("Try again")
            i -= 1
            continue
