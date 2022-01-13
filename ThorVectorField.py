from FinalTorusVectorField import *
from matplotlib import animation


fig = plt.figure(0)


def animatedplot(i):
    fig, ax, plot = plotAll(getTorusXYZ, 2, 1)
    print(i)
    ax.view_init(60-2*(i), 90*cos(4*pi*(i)/180)+60)


anim = animation.FuncAnimation(fig, animatedplot, 90, interval=30)
anim.save("VectorFieldTor.gif", writer="animation.HTMLWriter", fps=24, extra_args=['-vcodec', 'libx264'])
