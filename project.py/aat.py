from sympy import *
x,y = symbols('x y')
f=x*y+exp(y)
I = integrate(f,(x,3,4),(y,1,2))
print(I)

from sympy import *
x,y = symbols('x y')
f = x**2+y**2
I = integrate(f,(y,0,x),(x,0,1))
print(I)

from sympy import *
x,y,z = symbols('x y z')
f= x+y+z
I = integrate(f,(z,0,x+y),(y,0,x),(x,0,1))
print(I)