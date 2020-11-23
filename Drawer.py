import matplotlib.pyplot as plt
import numpy as np
plt.style.use("D:\library\presentation.mplstyle")

def Initial_Drawer(L_x,L_y,M,N,dx ,dy ):
	fig = plt.figure(figsize=(L_x,L_y))
	pox = 0.15
	poy = 0.15
	cpox = 0.88
	cpoy = poy
	#dx = 0.01
	#dy = 0.02
	xp = (0.9-pox)/(M) 
	yp = (0.9-poy)/(N) 
	cpx = 0.02
	cpy = N*(yp)-dy
	return fig,[pox,poy,xp,yp],[cpox,cpoy,cpx,cpy]

def Panel_Drawer(fig,m,n,dx,dy,data,p_info,f_info,cbmin,cbmax):
	pox = f_info[0] + m*f_info[2] 
	poy = f_info[1] + n*f_info[3] 
	xpanel = f_info[2] - dx
	ypanel = f_info[3] - dy
	x_min = p_info[0]
	x_max = p_info[1]
	y_min = p_info[2]
	y_max = p_info[3]
	ax = fig.add_axes([pox,poy,xpanel,ypanel])
	if(m != 0):
		plt.yticks([])
	if(n != 0):
		plt.xticks([])
	im = plt.imshow(data, extent=[x_min, x_max, y_min,y_max], origin='lower',cmap='jet',
		interpolation='bicubic',aspect='auto',vmin = cbmin,vmax = cbmax)
	return im

def Panel_Drawer2(fig,m,n,dx,dy,data,p_info,f_info,ylabel):
	pox = f_info[0] + m*f_info[2] 
	poy = f_info[1] + n*f_info[3] 
	xpanel = f_info[2] - dx
	ypanel = f_info[3] - dy
	x_min = p_info[0]
	x_max = p_info[1]
	y_min = p_info[2]
	y_max = p_info[3]
	ax = fig.add_axes([pox,poy,xpanel,ypanel])
	ax.clear()
	if(n != 0):
		plt.xticks([])
	t = np.linspace(x_min,x_max,len(data))
	plt.ylim([y_min,y_max])
	plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	if (m == 0):
		fig.text(0.04, poy+0.5*ypanel, ylabel, va='center', rotation='vertical',fontsize =22)
	im = plt.plot(t,data)
	return im
def Panel_Drawer3(fig,m,n,dx,dy,data,p_info,f_info,ylabel,j):
	pox = f_info[0] + m*f_info[2] 
	poy = f_info[1] + n*f_info[3] 
	xpanel = f_info[2] - dx
	ypanel = f_info[3] - dy
	x_min = p_info[0]
	x_max = p_info[1]
	y_min = p_info[2]
	y_max = p_info[3]
	t = np.linspace(x_min,x_max,len(data))
	ax = fig.add_axes([pox,poy,xpanel,ypanel])
	if(j == 0):
		#ax = fig.add_axes([pox,poy,xpanel,ypanel])
		#ax.clear()
		plt.ylim([y_min,y_max])
		plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	if (m == 0):
		fig.text(0.04, poy+0.5*ypanel, ylabel, va='center', rotation='vertical',fontsize =22)
	plt.plot(t,data)
def color_bar_add(fig,im,c_info):
	cbar_ax = fig.add_axes([c_info[0],c_info[1],c_info[2],c_info[3]])
	cb = fig.colorbar(im, cax = cbar_ax) 

def label_add(fig,xlabel,ylabel):
	fig.text(0.5, 0.04, xlabel, ha='center',fontsize =30)
	fig.text(0.01, 0.5, ylabel, va='center', rotation='vertical',fontsize =30)
