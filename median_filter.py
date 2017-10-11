import numpy as np

def median_filter(arr, winsize):
    if winsize%2 == 0:
        raise ValueError('winsize must be odd')
    arr=np.array(arr)
    out=np.zeros(len(arr))
    for i in range(len(arr)):
        filt_i = np.arange(i-winsize//2, i+1+winsize//2)
        for ix in range(len(filt_i)):
            if filt_i[ix] < 0:
                filt_i[ix] = 0
            elif filt_i[ix] >= len(arr):
                filt_i[ix] = len(arr)-1
        out[i] = np.median(arr[filt_i])
    return out