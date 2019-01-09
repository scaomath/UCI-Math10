from matplotlib import pyplot as plt
import numpy as np
# this library is for plotting in math 10
# adapted from Umut's math9 library

def drawfunction(f, imsize=200):
    # a 2 variable funciton surface
    arr = np.zeros([imsize,imsize])
    for i in range(imsize):
        for j in range(imsize):
            xx = (i - imsize/2) / imsize * 2
            yy = (-j + imsize/2) / imsize * 2
            arr[j,i] = f(xx,yy) 
    plt.imshow(arr, interpolation='nearest', cmap='gray', aspect = 'auto', vmin=0, vmax=1, extent=[-1,1,-1,1])
    plt.show()


def graphfunction(f, precision=300, x1=-1, x2=1, y1=-2, y2=2):
    # a one-var funciton
    arx = np.fromfunction(lambda i: ((i-precision/2)/precision*2), (precision, ))
    ary = np.vectorize(f)(arx) 
    plt.figure()
    plt.axis('auto')
    plt.grid(alpha = 0.6, linestyle='dashed')
    plt.plot(arx, ary, color = 'black', linewidth=4.0)
    plt.show()
    
