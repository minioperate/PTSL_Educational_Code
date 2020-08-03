import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys

sys.path.insert(1, 'D://library')
import diff as df
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
i_d = int(v*Nt*dt/dx)
k = 2*np.pi/((Nx)*dx)
x = np.linspace(0*dx,(Nx-1)*dx,Nx)
f = np.zeros((Nx,Nt))
f[:,0] = 3*np.sin(k*x)
ff = np.zeros(Nx)
ff[:] = 3*np.sin(k*x)
ffp = np.zeros(Nx)

def funcfp(f,fp,dx,t,BC,diff_type):
	for j in range(1,Nx-1):
		fp[j] = -A*(f[j+1]-f[j-1])/2 + B*(f[j+1]-2*f[j]+f[j-1])
	fp[0] =  -A*(f[1]-f[Nx-1])/2 + B*(f[1]-2*f[0]+f[Nx-1])
	fp[Nx-1] =  -A*(f[0]-f[Nx-2])/2 + B*(f[0]-2*f[Nx-1]+f[Nx-2])
for i in range(Nt-1):
	te.RK4(ff,ffp,funcfp,dt,dx,i*dt,BC='',diff_type = '')
	f[:,i+1] = ff[:]
plt.plot(x,f[:,0])
plt.plot(x,f[:,-1])
labels = ["initial condition", "Result"]
plt.legend(labels)
plt.xlabel("real space")
plt.ylabel("Amplitude")
plt.savefig("ADE-RK4.png")
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
plt.savefig("ADE-RK4-diff.png")
plt.show()
plt.plot(x,theo-f[:,-1])
plt.xlabel("real space")
plt.ylabel("Error")
plt.savefig("ADE-RK4-diff2.png")
plt.show()