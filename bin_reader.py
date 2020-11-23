import matplotlib as mpl
#mpl.use('Agg') # nodisplay X-windows with putty
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import sys
sys.path.append("D:/library")

class binary_reader(object):
	"""docstring for binary_reader"""
	def read_bin(self,rec,type,ndim):
		#f = open(fn,'rb')
		self.f.seek(rec)
		data = np.fromfile(self.f,dtype=type,count=ndim)
		return data
	def __init__(self):
		super(binary_reader, self).__init__()
		self.f = open('axis.bin','rb')
		bytes = 4
		self.nx   = self.read_bin(1*bytes,'int32',1)[0]
		self.ny   = self.read_bin(2*bytes,'int32',1)[0]
		self.nz   = self.read_bin(3*bytes,'int32',1)[0]
		self.nuex = self.read_bin(4*bytes,'int32',1)[0]
		self.nuey = self.read_bin(5*bytes,'int32',1)[0]
		self.nuez = self.read_bin(6*bytes,'int32',1)[0]
		self.nuix = self.read_bin(7*bytes,'int32',1)[0]
		self.nuiy = self.read_bin(8*bytes,'int32',1)[0]
		self.nuiz = self.read_bin(9*bytes,'int32',1)[0]
		self.nxyz = self.nx*self.ny*self.nz
		self.nuexyz = self.nuex*self.nuey*self.nuez
		self.nuixyz = self.nuix*self.nuiy*self.nuiz
		self.rx   = 14
		self.ruex = self.rx+2*(self.nx+self.ny+self.nz)
		self.ruix = self.ruex+2*(self.nuex+self.nuey+self.nuez)
		self.x    = self.read_bin(  self.rx*bytes,'float64',self.nx)
		self.uex  = self.read_bin(self.ruex*bytes,'float64',self.nuex)
		self.uix  = self.read_bin(self.ruix*bytes,'float64',self.nuix)
		print('initializer only read dimension size!')
		print('for reading different bins(d,f,e), you need call other function')
		print('for fluid : call flu_index_reader()')
	def flu_index_reader(self):
		self.rt  = 8
		self.rfex  = 15
		self.rfey  = self.rfex +2*self.nxyz*self.nuex+2
		self.rfez  = self.rfey +2*self.nxyz*self.nuey+2
		self.rfix  = self.rfez +2*self.nxyz*self.nuez+2
		self.rfiy  = self.rfix +2*self.nxyz*self.nuix+2
		self.rfiz  = self.rfiy +2*self.nxyz*self.nuiy+2
		self.rBx   = self.rfiz +2*self.nxyz*self.nuiz+2
		self.rBy   = self.rBx  +2*self.nxyz+2
		self.rBz   = self.rBy  +2*self.nxyz+2
		self.rEx   = self.rBz  +2*self.nxyz+2
		self.rEy   = self.rEx  +2*self.nxyz+2
		self.rEz   = self.rEy  +2*self.nxyz+2
		self.rRhoe = self.rEz  +2*self.nxyz+2
		self.rRhoi = self.rRhoe+2*self.nxyz+2
		self.rVex  = self.rRhoi+2*self.nxyz+2
		self.rVey  = self.rVex +2*self.nxyz+2
		self.rVez  = self.rVey +2*self.nxyz+2
		self.rVix  = self.rVez +2*self.nxyz+2
		self.rViy  = self.rVix +2*self.nxyz+2
		self.rViz  = self.rViy +2*self.nxyz+2
		self.rPex  = self.rViz +2*self.nxyz+2
		self.rPey  = self.rPex +2*self.nxyz+2
		self.rPez  = self.rPey +2*self.nxyz+2
		self.rPix  = self.rPez +2*self.nxyz+2
		self.rPiy  = self.rPix +2*self.nxyz+2
		self.rPiz  = self.rPiy +2*self.nxyz+2
	def dis_index_reader(self):
		print('wait for done')
	def fie_index_reader(self):
		self.rt = 8
		self.rBx = 13
		self.rBy = self.rBx+2*self.nxyz+2
		self.rBz = self.rBy+2*self.nxyz+2
		self.rEx = self.rBz+2*self.nxyz+2
		self.rEy = self.rEx+2*self.nxyz+2
		self.rEz = self.rEy+2*self.nxyz+2
	def flu_total_reader(self):
		with open('file_list_f.txt','rb') as f:
			first_line = f.readline()
			second_line= f.readline()
			offset = -50
			while True:
				f.seek(offset,2)
				lines = f.readlines()
				if len(lines) >= 2:
					last_line = lines[-1]
					break
				offset*=2
		a = int(first_line[1:11])
		b = int(second_line[1:11])
		c = int(last_line[1:11])
		diff = b-a
		leng = int((c-a)/(b-a)+1)
		self.f_name=[]
		for i in range(leng):
			n = str(i*diff)
			name = n.zfill(10)
			self.f_name.append('f'+name+'.bin')
	def fie_total_reader(self):
		with open('file_list_e.txt','rb') as f:
			first_line = f.readline()
			second_line= f.readline()
			offset = -50
			while True:
				f.seek(offset,2)
				lines = f.readlines()
				if len(lines) >= 2:
					last_line = lines[-1]
					break
				offset*=2
		a = int(first_line[1:11])
		b = int(second_line[1:11])
		c = int(last_line[1:11])
		diff = b-a
		leng = int((c-a)/(b-a)+1)
		self.e_name=[]
		for i in range(leng):
			n = str(i*diff)
			name = n.zfill(10)
			self.e_name.append('e'+name+'.bin')
	def dis_total_reader(self):
		print('wait to implement')
	def flu_one_reader(self,filename):
		self.f = open(filename,'rb')
		bytes=4
		self.f.seek(self.rt*bytes)
		tt = np.fromfile(self.f,dtype='float64',count=1)
		t = tt[0]
		fe = self.read_bin(self.rfex*bytes,'float64',self.nx*self.nuex).reshape((self.nx,self.nuex))
		datae=np.zeros((self.nuex,self.nx))
		for ix in range(0, self.nx, 1): 
			for iu in range(0, self.nuex, 1):
				datae[iu,ix] = fe[ix,iu]
		Ex     = read_bin(self.rEx*bytes,'float64',self.nx)
		return t,datae,Ex
	def dis(self):
		self.dis_index_reader()
		self.dis_total_reader()
		print('start to call draw function')
	def flu(self):
		self.flu_index_reader()
		self.flu_total_reader()
		print('start to call draw function')
	def fie(self):
		self.fie_index_reader()
		self.fie_total_reader()
		print('start to call draw function')

class Drawer(binary_reader):
	"""docstring for Drawer"""
	def __init__(self,xfigsize,yfigsize,pox,poy,xpl,ypl,dypl,x_min,x_max,y_min,y_max,cb_min,cb_max):
		super(Drawer, self).__init__()
		plt.style.use('D:/library/presentation.mplstyle')
		#plt.style.use('./presentation.mplstyle')
		# plot setting
		self.xfigsize = xfigsize
		self.yfigsize = yfigsize
		self.pox = pox
		self.poy = poy
		self.xpl = xpl
		self.ypl = ypl
		self.dypl = dypl
		self.x_max=x_max
		self.x_min=x_min
		self.y_max=y_max
		self.y_min=y_min
		self.cb_max=cb_max
		self.cb_min=cb_min
		self.asp = yfigsize*ypl*(x_max-x_min)/(xfigsize*xpl*(y_max-y_min))
		self.cbpox = pox+xpl+0.02*xpl
		self.cbpoy = poy
		self.cbxpl = 0.025*xpl
		self.cbypl = ypl

	def Drawer_2D(self,xtitle,ytitle,title,cbtitle,data,filename):
		fig1 = plt.figure(figsize=(self.xfigsize,self.yfigsize))
		fig = plt.gcf()    
		#fig.set_size_inches(self.xfigsize,self.yfigsize)
		ax = fig.add_axes([self.pox, self.poy, self.xpl, self.ypl])
		#    data = np.flipud(data)  # Don't use this command when using pcolormesh 
		ax.set_title(title)
		ax.set_xlabel(xtitle)
		ax.set_ylabel(ytitle)
		#plt.axis([self.x_min, self.x_max, self.y_min, self.y_max])

		im = plt.imshow(data, vmin=self.cb_min, vmax=self.cb_max,
		            extent=[self.x_min, self.x_max, self.y_min,self.y_max], aspect=self.asp) #, zorder=1)
		#  plot color bar
		#cb = fig.add_axes([self.cbpox,self.cbpoy,self.cbxpl,self.cbypl])
		#cbar = plt.colorbar(im, cax=cb)
		cbar = plt.colorbar(im)
		cbar.ax.set_ylabel(cbtitle)
		plt.sca(ax)
		#plt.savefig(filename)
		#plt.show()

