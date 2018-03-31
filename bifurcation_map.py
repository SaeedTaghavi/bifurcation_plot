import numpy as np
from matplotlib import pyplot as plt

# this simple code produces bifurcation diagram for different nonliniear maps.

# range command just accepts integer numbers, this function defines a my_range command
#  that accepts float numbers
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

# this function defines different chaotic maps,
# name argument specifies the name of the map, here I have defined logistic, tent, ecology, and gaussian map
# m is a real number which is known as the control parameter of maps
# x is a real number which is the output of the map.
def maps(name,  m , x):
    if name == 'logistic':
        #in this definition m varies [0,4]
        return m * x * (1.0 - x)
    if name == 'tent':
        if x < 0.5:
            # in this definition m varies [1,2]
            return m* x
        if x > 0.5:
            return m * (1.0 - x)
    if name =='ecology':
        return x * np.exp( m * ( 1.0 - x ) )
    if name == 'gaussian':
        b = 5.0    # b is a free parameter in gaussian map that could be a real number
                   # b could be treated as an other bifurcation parameter of the map
        return np.exp(-b * x * x) + m

# this function plots the bifurcation diagram for a map
# name specifies the name of the map
# m_min and m_max  represent the m parameter's domain(which is the control parameter of the map)
# step is the step of m parameter
def plot_bifurcation(name, m_min, m_max, step):
    fig = plt.figure()
    x = 0.25
    map_name = name
    for m in my_range(m_min, m_max , step):
        for i in range (1,501,1):   #skip transients
            x = maps(map_name , m , x)
        for i in range (1,50,1):
            x = maps(map_name, m, x)
            plt.plot(m,x,'r,')
    plt.xlabel('m')
    plt.ylabel('x')
    # plt.legend()
    plt.title('Bifurcation diagram for the %s map ' % (map_name))
    # plt.show()
    fig.savefig('%s_map.png' % (map_name))

# plot_bifurcation('map name',m_min , m_max , step_m)
# map name: logistic, tent, ecology
plot_bifurcation('tent',1.0 , 2.0 , .01)
