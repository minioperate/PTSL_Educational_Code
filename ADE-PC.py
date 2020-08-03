import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys

sys.path.insert(1, 'D://library')
from diff import *
import time_evolution as te
mpl.style.use("D:\\library\\presentation.mplstyle")
dx = 0.1
dt = 0.001
v = 1
D = 1
A = v/dx
B = D/dx**2
Nx = 100
Nt = 1000
dff = diff('periodic',Nx)
i_d = int(v*Nt*dt/dx)
k = 2*np.pi/((Nx)*dx)
x = np.linspace(0*dx,(Nx-1)*dx,Nx)
f = np.zeros((Nx,Nt))
f[:,0] = 3*np.sin(k*x)
ff = np.zeros(Nx)
ff[:] = 3*np.sin(k*x)
ffp = np.zeros(Nx)

def funcfp(f,fp,dx,t,BC,diff_type):
	f_t = np.zeros(len(f))
	dff.diff(f,f_t,dx,'central')
	f_tt = np.zeros(len(f))
	dff.diff(f_t,f_tt,dx,'central')
	for j in range(Nx):
		fp[j] = -v*f_t[j] + D*f_tt[j]
	#fp[0] =  -A*(f[1]-f[Nx-1])/2 + B*(f[1]-2*f[0]+f[Nx-1])
	#fp[Nx-1] =  -A*(f[0]-f[Nx-2])/2 + B*(f[0]-2*f[Nx-1]+f[Nx-2])

f1 = np.zeros(Nx)
f2 = np.zeros(Nx)
f3 = np.zeros(Nx)
for t in range(Nt-1):
	print(t)
	if(t == 0):
		funcfp(ff,ffp,dx,t*dt,BC='periodic',diff_type = '')
	for i in range(Nx):
		f3[i] = ffp[i]
	if(t<3):
		te.RK4(ff,ffp,funcfp,dt,dx,i*dt,BC='',diff_type = '')
		if(t == 1):
			for i in range(Nx):
				f2[i] = ffp[i]
		elif(t == 2):
			for i in range(Nx):
				f1[i] = ffp[i]
	else:
		#te.RK4(u,du,funcfp,dt,dx,t*dt,BC='periodic',diff_type = types)
		te.PC_Adam(ff,ffp,funcfp,dt,f1,f2,f3,dx,t*dt,BC='periodic',diff_type = '')
	f[:,t+1] = ff[:]
plt.plot(x,f[:,0])
plt.plot(x,f[:,-1])
labels = ["initial condition", "Result"]
plt.legend(labels)
plt.xlabel("real space")
plt.ylabel("Amplitude")
plt.savefig("ADE-PC.png")
plt.show()
theo = np.zeros(Nx)
for i in range(Nx):
	ii = i - i_d
	if ii <0:
		ii = ii + Nx
	theo[i] = f[ii,0]*np.exp(-D*k**2*(Nt+1)*dt) 
plt.plot(x,theo)
plt.plot(x,f[:,-1])
labels = ["Theory", "Result"]
plt.legend(labels)
plt.xlabel("real space")
plt.ylabel("Amplitude")
plt.savefig("ADE-PC-diff.png")
plt.show()
plt.plot(x,theo-f[:,-1])
plt.xlabel("real space")
plt.ylabel("Error")
plt.savefig("ADE-PC-diff2.png")
plt.show()