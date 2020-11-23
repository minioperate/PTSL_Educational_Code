import numpy as np
class parameter(object):
	"""docstring for parameter"""
	def __init__(self, KE, ratio_n, wave_length):
		super(parameter, self).__init__()
		self.c = 2.99792458e8
		self.me = 9.1093837015e-31
		self.qe = 1.60217662e-19
		self.ep0 = 8.8541878123e-12
		self.mu0 = 1.2566370614e-6
		self.mecc = self.me*self.c**2/self.qe
		gamma = 1+(KE/2)/self.mecc
		self.ratio_v = np.sqrt((1-1/gamma**2)**(-1))
		self.vth = self.c/self.ratio_v
		self.l_wave = wave_length
		self.k_wave = 2*np.pi/self.l_wave
		self.w_wave = self.c*self.k_wave
		self.n_c = self.w_wave**2*self.me*self.ep0/self.qe**2
		self.n_e = ratio_n*self.n_c
		self.wpe = np.sqrt(self.n_e*self.qe**2/(self.me*self.ep0))
		self.ratio_w = self.w_wave/self.wpe
		self.debye = self.vth/self.wpe
		self.ratio_l = self.l_wave/self.debye
		self.E_0 = self.me*self.vth*self.wpe/self.qe
		self.B_0 = self.me*self.wpe/self.qe
		self.wb = np.sqrt(self.qe*self.E_0*(2*np.pi/self.debye)/self.me)
	def I_to_EB(self,I):
		E = np.sqrt(2*self.c*self.mu0*I)
		B = np.sqrt(2*self.mu0*I/self.c)
		print("Normalized E of I = "+str(I)+" is "+str(E/self.E_0))
		print("Normalized B of I = "+str(I)+" is "+str(B/self.B_0))
		return(E/self.E_0,B/self.B_0)
	def print_quantity(self):
		print("c/vth is "+str(self.ratio_v))
		print("w_wave/wpe is "+str(self.ratio_w))
		print("L_wave/L_D is "+str(self.ratio_l))
	def E_to_I(self,E):
		I = (E*self.E_0)**2/(2*self.c*self.mu0)
		I = I/1e4
		print("laser intensity with normalized E : %f is related to %e W/cm^2" %(E,I))
