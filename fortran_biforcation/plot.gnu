set term png size 800,600 font "Times,20"
set key off
set xlabel "r"
set ylabel "x"

set output 'bifurcation.png'

p 'results.dat' w d 

