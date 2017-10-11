import numpy as np


def gauss_kern(x0, x, b):
    return np.exp(-(x0-x)**2/(2*b**2))
    

def gauss_smooth(x, y, l):
    y = np.array(y)
    x = np.array(x)
    b = np.ptp(x)/(len(x)-1)*np.sqrt(2)
    xsmoothed = np.linspace(np.min(x), np.max(x), l)
    smoothed = np.zeros(l)
    for i in range(len(smoothed)):
        kvec = gauss_kern(xsmoothed[i], x, b)
        smoothed[i] = np.sum(kvec*y)/np.sum(kvec)
    return xsmoothed, smoothed