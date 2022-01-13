from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from numpy import sin, cos, pi, arange, array, meshgrid


def getAll(n, k):
    if n**2+k**2 == 0:
        m = 1
    else:
        m = max(n, k)
    u = arange(-m, m+0.05, 0.05)
    v = arange(0, 4.05, 0.05)
    u, v = meshgrid(u, v)
    du = cos(pi*u*((n+k) - (n-k)*sin(pi*v/2)) / (2*m))
    dv = cos(pi*v/2)
    return u, v, du, dv


def getTorusXYZ(u, v, m):
    u, v = u/m, v/4
    x = (3 + cos(2*pi * v))* cos(pi * u)
    y = (3 + cos(2*pi * v))* sin(pi * u)
    z = sin(2*pi * v)
    return x, y, z


def initFig():
    fig = plt.figure(0)
    fig.patch.set_facecolor('#2F2F2F')

    ax = fig.add_subplot(121, projection='3d', xlim=(-4, 4), ylim=(-4, 4), zlim=(-4, 4))
    plot = fig.add_subplot(122)

    ax.set_axis_off()

    ax.set_facecolor('k')
    plot.set_facecolor('k')

    fig.set_figwidth(16)
    fig.set_figheight(16)
    return fig, ax, plot


def plotAll(surface, n, k, field=getAll, plotSurface=False):
    fig, ax, plot = initFig()
    u, v, du, dv = field(n, k)
    if n**2+k**2 == 0:
        m = 1
    else:
        m = max(n, k)

    if plotSurface:
        x, y, z = surface(u, v, m)
        ax.plot_surface(x, y, z, color='purple', alpha=0.25)

    # 2D
    plot.quiver(u, v, du, dv, color='b')
    container = plot.streamplot(u, v, du, dv, color='r', linewidth=0.5, density=3)

    # 3D
    segments = container.lines.get_segments()
    for line in segments:
        ixs, iys, izs = surface(array([line[0][0], line[1][0]]), array([line[0][1], line[1][1]]), m)
        color = 'b'
        for z in izs:
            if z > 0:
                color = 'r'
        Axes3D.plot(ax, ixs, iys, izs, color=color, lw=0.5)

    return fig, ax, plot


if __name__ == '__main__':
    i = 0
    while True:
        try:
            n = int(input('number of inlets: '))
            k = int(input('number of outlets: '))
            fig, ax, plot = plotAll(getTorusXYZ, n, k)
            ax.view_init(30, 117)
            plt.savefig("temp/torus/tempt{}.png".format(i))
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

