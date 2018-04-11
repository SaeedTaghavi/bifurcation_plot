program bifurcation
implicit real(a-h,o-z)
open (1,file='results.dat')
r=0.0
do while (r<1.)
	x=.8
	!write (1,*)r,x
	do i=1,10000
		x=4*r*x*(1-x)
		if (i>9900) then
			write(1,*)r,x
		end if
	end do
	r=r+.0001
end do
call system ('gnuplot plot.gnu')
call system ('display bifurcation.png')
end program bifurcation
