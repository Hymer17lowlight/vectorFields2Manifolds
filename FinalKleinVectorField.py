import matplotlib.pyplot as plt
from numpy import sin, cos, pi
from mpl_toolkits.mplot3d import Axes3D
from FinalTorusVectorField import plotAll


def getBottleXYZ(u, v, m):
    u, v = pi*u/m, pi*v/2
    x = (3 + cos(u)) * cos(v)
    y = (3 + cos(u)) * sin(v)
    z = sin(u) * cos(v / 2)
    return x, y, z


if __name__ == '__main__':
    i = 0
    while True:
        try:
            n = int(input('number of inlets: '))
            k = int(input('number of outlets: '))
            fig, ax, plot = plotAll(getBottleXYZ, n, k)
            ax.view_init(35, 114)
            plt.savefig("temp/bottle/tempb{}.png".format(i))
            plt.show()
            i += 1

            ax.set_axis_off()

            ax.set_facecolor('k')
            plot.set_facecolor('k')
        except IndexError:
            print("It's impossible")
            i -= 1
            continue
        except ValueError:
            print("Try again")
            i -= 1
            continue
