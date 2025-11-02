from sympy.vector import *
from sympy import *
C = CoordSys3D (' ') # Setting the coordinate system
x,y,z = C.x, C.y,C.z # Variables x,y,z to be used with coordinate system C
A=x**2*y+z
delop = Del() #Del operator
gradA=delop(A) # substitution of A in the Del operatore
gradA_sim = gradA.doit()
print('grad A is =',gradA,'=', gradA_sim)

from sympy.vector import *
C= CoordSys3D (' ')
x,y,z = C.x, C.y,C.z
i,j,k = C.i,C.j,C.k
vecF=(2*x**2*z)*i-(x*y**2*z)*j+(3*y*z**2)*k
delop=Del()
divF = delop.dot(vecF)
divF_sim = divF.doit()
print('div vec F =',divF,'=',divF_sim)

from sympy.vector import *
C= CoordSys3D (' ')
x,y,z = C.x, C.y,C.z
i,j,k = C.i,C.j,C.k
vecF=(2*x**2*z)*i-(x*y**2*z)*j+(3*y*z**2)*k
delop = Del()
CurlF = delop.cross(vecF)
CurlF_sim = CurlF.doit() # or use CurlF = curl(vecF)
print('Curl F = ',CurlF,'=',CurlF_sim)