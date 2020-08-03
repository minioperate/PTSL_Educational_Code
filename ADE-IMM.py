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
A = v*dt/dx
B = D*dt/dx**2
Nx = 100
Nt = 1000
i_d = int(v*Nt*dt/dx)
#k = 2*np.pi/(0.5*Nx*dx)
x = np.linspace(0*dx,(Nx-1)*dx,Nx)
k = 2*np.pi/(Nx*dx)
f = np.zeros((Nx,Nt))
f[:,0] = 3*np.sin(k*x)
AA = np.zeros((Nx,Nx))
eta2 = 1+A+2*B
eta1 = -A-B
eta3 = -B
print(eta1,eta2,eta3)
for i in range(1,Nx-1):
	AA[i-1,i] = eta1
	AA[i,i] = eta2
	AA[i+1,i] = eta3
AA[0,0] = eta2
AA[1,0] = eta3
AA[-1,0]= eta1
AA[-1,-1] = eta2
AA[-2,-1] = eta1
AA[0,-1]  = eta3

AA_T = np.linalg.inv(np.transpose(AA))

for i in range(Nt-1):
	f[:,i+1] = np.dot(AA_T,f[:,i])
plt.plot(x,f[:,0])
plt.plot(x,f[:,-1])
labels = ["initial condition", "Result"]
plt.legend(labels)
plt.xlabel("real space")
plt.ylabel("Amplitude")
plt.savefig("ADE-IMM.png")
plt.show()
theo = np.zeros(Nx)
for i in range(Nx):
	ii = i - i_d
	if ii <0:
		ii = ii + Nx
	theo[i] = f[ii,0]*np.exp(-D*k**2*(Nt)*dt) 
plt.plot(x,theo)
plt.plot(x,f[:,-1])
labels = ["Theory", "Result"]
plt.legend(labels)
plt.xlabel("real space")
plt.ylabel("Amplitude")
plt.savefig("ADE-IMM-diff.png")
plt.show()
plt.plot(x,theo-f[:,-1])
plt.xlabel("real space")
plt.ylabel("Error")
plt.savefig("ADE-IMM-diff2.png")
plt.show()
