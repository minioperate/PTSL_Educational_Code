import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use("D:\\library\\presentation.mplstyle")
dx = 0.1
dt = 0.001
v = 1
D = 0
A = v*dt/dx
B = D*dt/dx**2
Nx = 100
Nt = 1000
i_d = int(v*Nt*dt/dx)
k = 2*np.pi/(Nx*dx)
x = np.linspace(0*dx,(Nx-1)*dx,Nx)
f = np.zeros((Nx,Nt))
f[:,0] = 3*np.sin(k*x)
for i in range(1,Nt):
	for j in range(1,Nx-1):
		f[j,i] = f[j,i-1] - A*(f[j+1,i-1]-f[j-1,i-1])/2 + B*(f[j+1,i-1]-2*f[j,i-1]+f[j-1,i-1])
	f[0,i] = f[0,i-1] - A*(f[1,i-1]-f[Nx-1,i-1])/2 + B*(f[1,i-1]-2*f[0,i-1]+f[Nx-1,i-1])
	f[Nx-1,i] = f[Nx-1,i-1] - A*(f[0,i-1]-f[Nx-2,i-1])/2 + B*(f[0,i-1]-2*f[Nx-1,i-1]+f[Nx-2,i-1])
plt.plot(x,f[:,0])
plt.plot(x,f[:,-1])
labels = ["initial condition", "Result"]
plt.legend(labels)
plt.xlabel("real space")
plt.ylabel("Amplitude")
plt.savefig("ADE-Euler.png")
plt.show()
theo = np.zeros(Nx)
for i in range(Nx):
	ii = i - i_d
	if ii <0:
		ii + Nx
	theo[i] = f[ii,0]*np.exp(-D*k**2*Nt*dt) 
plt.plot(x,theo)
plt.plot(x,f[:,-1])
labels = ["Theory", "Result"]
plt.legend(labels)
plt.xlabel("real space")
plt.ylabel("Amplitude")
plt.savefig("ADE-Euler-diff.png")
plt.show()
plt.plot(x,theo-f[:,-1])
plt.xlabel("real space")
plt.ylabel("Error")
plt.savefig("ADE-Euler-diff2.png")
plt.show()