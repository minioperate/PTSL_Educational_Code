from mpmath import *
from numpy import complex
import numpy as np
from numpy import *
from scipy.special import erf
from scipy.special import wofz

def complex_root_solver(x,para,step,converge,D):
	#x        : the root you want to solve
	#para     : other parameter u will use in the function D
	#step     : how big the step u will step
	#converge : converge condition when abs(D)<converge
	done = 0
	while(abs(D(x,para))>converge and done<300):
		J1 = (D(x+1e-6,para)-D(x,para))/1e-6
		J2 = (D(x+1e-6j,para)-D(x,para))/1e-6
		J11 = J1.real
		J12 = J2.real
		J21 = J1.imag
		J22 = J2.imag
		J = [J11,J12],[J21,J22]
		Jacobian = mat(J)
		inver_J = Jacobian.I
		aa = [D(x,para).real,D(x,para).imag]
		a1 = mat(aa)
		a2 = a1.T
		bb = [x.real,x.imag]
		b1 = mat(bb)
		b2 = b1.T
		b2 = b2 - inver_J*a2*step
		x = complex(b2[0,0],b2[1,0])
		done = done + 1
	if( abs(D(x,para))>converge or D(x,para).real>1e20 or D(x,para).imag>1e20 or math.isnan(D(x,para).real)or math.isnan(D(x,para).imag)):
		return complex(0,0)
	else:
		print('done !, x is ',x,' and parameter is ',para,',and done is',done)
		return x


def Z(k,w,a,con):
    i = complex(0.0,1.0)
    return i*math.sqrt(math.pi)*wofz((w/k+a)*con)

def BOTI_D(w,k):
	a = complex(4.5,0)
	con = complex(1/(math.sqrt(2)),0)
	con2 = complex(1/(0.5*math.sqrt(2)),0)
	x1 = (w/k+0)*con
	x2 = (w/k-a)*con2
	return 0.25+(0.9*0.25*(1+x1*Z(k,w,0,con))+0.2*(1+x2*Z(k,w,-1.0*a,con2)))/(k*k)

def LD_D(w,k):
	a = complex(0,0)
	con = complex(1/np.sqrt(2),0)
	return 1+(1/k**2)*(1+(w/(np.sqrt(2)*k))*Z(k,w,a,con))

def TSI_TypeI_D(w,k):
	z=(w/(np.sqrt(2)*k))
	a = complex(0,0)
	con = complex(1/np.sqrt(2),0)
	return 1-(1/k**2)*(1-2*z**2+2*Z(k,w,a,con)*(z-z**3))
def TSI_TypeII_D(w,k):
	a = complex(-1,0)
	con = complex(1/(math.sqrt(2)),0)
	x1 = (w/k+a)*con
	x2 = (w/k-a)*con
	return 1+(0.5*(1+x1*Z(k,w,a,con))+0.5*(1+x2*Z(k,w,-1.0*a,con)))/(k*k)
def Weibel_D(w,para):
	k = para[0]
	c = para[1]
	con = complex(1/(math.sqrt(2)),0)
	a = complex(0,0)
	x1 = (w/k)*con
	coeff1 = 1/(c**2*k**2)
	coeff2 = 1/c**2
	return -0.5+coeff1*x1*Z(k,w,a,con)+coeff2*x1**2
def Weibel_2_D(w,para):
	k = para[0]
	c = para[1]
	con = complex(1/(math.sqrt(2)),0)
	a = complex(0,0)
	x1 = (w/k)*con
	coeff1 = (c**2*k**2)/w**2
	coeff2 = 1/w**2
	return 1-coeff1+coeff2*(x1*Z(k,w,a,con)*10+9)