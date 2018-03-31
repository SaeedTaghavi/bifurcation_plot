import numpy as np
from matplotlib import pyplot as plt

#this is a simple code to produce a bifurcation diagram of the Gaussian map.
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

m_min = -1.0;    m_max = +1.0;    step = 0.005
lastx = int(1000*0.5)
count = 0

bs = [1.0 , 4.0 , 5.0 , 6.2]
for b in bs:
    fig = plt.figure()
    for m in my_range(m_min , m_max , step):
        x = 0.5
        for i in range (1, 401 , 1):
            x = np.exp(-b * x * x) + m
        for i in range (201, 402 , 1):
            x = np.exp(-b * x * x) + m
            intx = int (1000*x)
            if intx != lastx and count%2==0:
                plt.plot(m,x,'r,' , label='b= %s' % (b))
            lastx = intx
            count += 1
    plt.xlabel('m')
    plt.ylabel('x')
    plt.legend()
    plt.title('Bifurcation diagram for the Guassian map with b= %s' % (b))
    # plt.show()
    fig.savefig('b=%s.png'%(b))






