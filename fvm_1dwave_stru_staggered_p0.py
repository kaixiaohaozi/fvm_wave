import numpy as np
import matplotlib.pyplot as plt


def wave1d(x, t):
    dx = x[1]-x[0]
    dt = t[1]-t[0]
    
    l = 5
    k = np.pi*2/1.064
    c = 5
    rou = 1

    y = np.zeros([len(t), len(x)])
    y[0, x < l] = np.sin(k*x[x<l])*np.sin(np.abs(x[x<l]*np.pi/l))
    v = np.zeros([len(t), len(x)-1])
     
    for i in range(1, len(t)):

        v[i,:] = (y[i-1, :-1]-y[i-1, 1:])/rou/dx*dt + v[i-1,:]
        y[i,1:-1] = (c**2)*rou*(v[i, :-1]-v[i, 1:])/dx*dt + y[i-1,1:-1]
        y[i,0] = y[i,-1] = 0.

    return y


import matplotlib.animation as animation
# 输入时间，自变量，因变量，图题标记
def drawGif(t,x,ys,mark="time="):
    tAxis = np.linspace(0,len(t)-1,100).astype(int)

    fig = plt.figure()
    ax = fig.add_subplot(111,xlim=(0,10),ylim=(-1.5,1.5))
    ax.grid()

    line, = ax.plot([],[],lw=0.2)
    time_text = ax.text(0.1,0.9,'',transform=ax.transAxes)

    def init():
        line.set_data([],[])
        time_text.set_text("")
        return line, time_text
    
    def animate(i):
        y = ys[i]
        line.set_data(x,y)
        time_text.set_text(mark+str(t[i]))
        return line, time_text

    # 动态图绘制命令
    # 输入分别为画图窗口，动画函数，动画函数输入变量，延时，初始函数
    ani = animation.FuncAnimation(fig, animate, tAxis, interval=200, init_func=init)
    ani.save(r'D:\【资料】\【读研】命运的洪流\做学术做得想薯\代码\v1ssp.gif',writer='pillow')
    plt.show()


if __name__ == "__main__":
    x = np.linspace(0,10,501)
    t = np.linspace(0,4,2000)

    y = wave1d(x,t)
    drawGif(t,x,y)

 