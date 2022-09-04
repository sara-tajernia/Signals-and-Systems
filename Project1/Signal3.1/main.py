import numpy as np
import matplotlib.pyplot as plt

def function1():

    def yt1(t, a):
        return 0

    def yt2(t, a):
        return t + a

    def yt3(t, a):
        return -t-a

    t_T, x_t_T = [], []
    for k in range(3):
        t, t1, t2, t3, t4 = [], [], [], [], []
        for i in range ((4*k-6),(4*k-4)): t1.append(i)
        for i in range ((4*k-5),(4*k-3)): t2.append(i)
        for i in range ((4*k-4),(4*k-2)): t3.append(i)
        for i in range ((4*k-3),(4*k-1)): t4.append(i)
        y1 = np.vectorize(yt1, otypes=[float])(t1, 0)
        y2 = np.vectorize(yt2, otypes=[float])(t2, 5-(4*k))
        y3 = np.vectorize(yt3, otypes=[float])(t3, 3-(4*k))
        y4 = np.vectorize(yt1, otypes=[float])(t4, 0)
        t = np.concatenate([t1, t2, t3, t4])
        x_t = np.concatenate([y1, y2, y3, y4])
        t_T = np.concatenate([t_T, t])
        x_t_T = np.concatenate([x_t_T, x_t])
    plt.plot(t_T, x_t_T)
    plt.show()
    return t_T, x_t_T

def function2():
    def yt(t, a):
        return t + a
    t, t1 , t2, t3=[], [], [], []
    for i in range (-6,-1): t1.append(i)
    for i in range (-2,3): t2.append(i)
    for i in range (2,7): t3.append(i)
    y1 = np.vectorize(yt, otypes=[float])(t1, 4)
    t = np.concatenate([t1, t2, t3])
    x_t = np.concatenate([y1, y1, y1])
    plt.plot(t, x_t)
    plt.show()

    return t, x_t


def fourie(wave,k1, k2, T):
    omega = np.pi * 2 / T
    ak = []
    for i in range(k1, k2):
        bk, ck = 0, 0
        for s in range(T - 1):
            bk += wave[s] * np.cos(s * i * omega)
            ck += wave[s] * np.sin(s * i * omega)
        bk *= 1 / T
        ck *= 1 / T
        ak.append(complex(bk, -ck))
    for z in range(len(ak)):
        ak[z] = abs(ak[z])
    time = np.linspace(0, T, k2-k1)
    plt.stem(time, ak + bk)
    plt.show()

if __name__ == '__main__':
    t1, x_t1 = function1()
    fourie(x_t1, 0, 2, t1.shape[0])
    fourie(x_t1, 0, 10, t1.shape[0])
    fourie(x_t1, 0, 50, t1.shape[0])
    fourie(x_t1, 100, 200, t1.shape[0])
    t2, x_t2 = function2()
    fourie(x_t2, 0, 2, t2.shape[0])
    fourie(x_t2, 0, 10, t2.shape[0])
    fourie(x_t2, 0, 50, t2.shape[0])
    fourie(x_t2, 100, 200, t2.shape[0])
