from numpy import arange, sin, cos, pi, meshgrid
from matplotlib import pyplot as plt
from matplotlib import animation


def getUV1(u, v):
    du = sin(pi*(u-v))
    dv = cos(pi*(u+v))
    return du, dv


def getUV2(u, v):
    du = cos(pi*(u))
    dv = cos(pi*(v))
    return du, dv


def getUV3(u, v, a=0):
    du = cos((pi + a) * v)
    dv = cos(pi * u)
    return du, dv


def getUV31(u, v):
    du, dv = getUV3(u, v, a=0.5)
    return du, dv

def getUV4(u, v):
    du = 0*u
    dv = (2-v)**2
    return du, dv


def getUV5(u, v):
    du = sin(3*pi*u)
    dv = sin(pi*v/2)
    return du, dv


def getUVInlet(u, v):
    return u, v-2


def getUVpr(u, v, n=2):
    du = sin(n * pi * u)
    dv = sin(n * pi * v)
    return du, dv


def getUVios(u, v, n=2):
    du = sin(n * pi * u)
    dv = -sin(n * pi * v)
    return du, dv


def plotField(vectorFieldFunction):
    plot = fig.gca()
    plt.cla()
    u = arange(-1, 1.05, 0.05)
    v = arange(0, 4.05, 0.05)
    if vectorFieldFunction==getUVpr or vectorFieldFunction==getUVios:
        v = arange(-1, 1.05, 0.05)
    u, v = meshgrid(u, v)
    du, dv = vectorFieldFunction(u, v)
    plot.quiver(u, v, du, dv)
    plot.streamplot(u, v, du, dv, color='r', linewidth=1)
    plt.show()


def animated(i):
    print(i)

    def getuv(u, v):
        du, dv = getUV3(u, v, a=i/90)
        return du, dv

    plotField(getuv)


if __name__ == "__main__":
    fig = plt.figure(0)
    """anim = animation.FuncAnimation(fig, animated, 90, interval=30)
    anim.save("VectorFieldPer.gif", writer="animation.HTMLWriter", fps=12, extra_args=['-vcodec', 'libx264'])"""
    plotField(getUVios)

