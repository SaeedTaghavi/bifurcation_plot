This is a python code to plot the bifurcation diagram for several well-known maps in mathematics, also a ample fortran code is available to produce bifurcation diagram just for logistic maps, but it can be easily changed in the source of the code. 

take Gaussian map as an example for more explanations:


In mathematics, the Gauss map (also known as Gaussian map or mouse map), is a nonlinear iterated map of the reals into a real interval given by the Gaussian function:

x[n+1] = exp(-b * x[n] * x[n]) + m

where b and m are real parameters.

In the parameter real space x[n] can be chaotic. The map is also called the mouse map because its bifurcation diagram resembles a mouse (see Figures).

This python script will plot bifurcation diagram of the Gaussian map for different values of b.

It is a good example for plotting and adding legend, title, axis label to a plot in python.

| !![bifurcation diagram using fortran](https://github.com/SaeedTaghavi/bifurcation_plot/blob/master/fortran_biforcation/bifurcation.png)
 | 
|:--:| 
| *bifurcation diagram for the logistic map using the fortran code* |

<p align="center">
  <img src="https://github.com/SaeedTaghavi/bifurcation_plot/blob/master/b%3D4.0.png" width="400"/>
  <img src="https://github.com/SaeedTaghavi/bifurcation_plot/blob/master/b%3D5.0.png" width="400"/>
</p>
