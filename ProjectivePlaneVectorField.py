from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from numpy import sin, cos, pi, arange, array, meshgrid, sqrt


def getAll(n):
    u = arange(-1, 1+0.01/n, 0.01/n)
    v = arange(-1, 1+0.01/n, 0.01/n)
    u, v = meshgrid(u, v)
    du = sin(n*pi*u)
    dv = -sin(n*pi*v)
    return u, v, du, dv


def getBoyXYZ(u, v):
    u, v = pi*u, pi*v
    x = 4*cos(u)*((sqrt(2) / 3)*cos(u)*cos(2*v) + (2/3)*sin(u)*cos(v))/(1 - sqrt(2)*sin(u)*cos(u)*sin(3*v))
    y = 4*cos(u)*((sqrt(2) / 3)*cos(u)*sin(2*v) - (2/3)*sin(u)*sin(v))/(1 - sqrt(2)*sin(u)*cos(u)*sin(3*v))
    z = 4*cos(u)*cos(u)/(1 - sqrt(2)*sin(u)*cos(u)*sin(3*v))-4
    return x, y, z


def initFig(i):
    fig = plt.figure(i)
    fig.patch.set_facecolor('#2F2F2F')

    ax = fig.add_subplot(121, projection='3d', xlim=(-4, 4), ylim=(-4, 4), zlim=(-4, 4))
    plot = fig.add_subplot(122)

    ax.set_axis_off()

    ax.set_facecolor('k')
    plot.set_facecolor('k')

    fig.set_figwidth(16)
    fig.set_figheight(16)
    return fig, ax, plot


def plotAll(surface, n, i, field=getAll, plotSurface=False):
    fig, ax, plot = initFig(i)
    u, v, du, dv = field(n)

    if plotSurface:
        x, y, z = surface(u, v)
        ax.plot_surface(x, y, z, color='purple', alpha=0.25)

    # 2D

    plot.quiver(u, v, du, dv, color='b')
    container = plot.streamplot(u, v, du, dv, color='r', linewidth=0.5, density=1.5)

    # 3D
    segments = container.lines.get_segments()
    for line in segments:
        ixs, iys, izs = surface(array([line[0][0], line[1][0]]), array([line[0][1], line[1][1]]))
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
            n = int(input('a: '))
            fig, ax, plot = plotAll(getBoyXYZ, n, i)
            ax.view_init(220, 161)
            plt.savefig("temp/Boy/tempB{}_f1.png".format(i))
            fig, ax, plot = plotAll(getBoyXYZ, n, i)
            ax.view_init(41, 161)
            plt.savefig("temp/Boy/tempB{}_f2.png".format(i))
            fig, ax, plot = plotAll(getBoyXYZ, n, i)
            ax.view_init(90, 161)
            plt.savefig("temp/Boy/tempB{}_f3.png".format(i))
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

