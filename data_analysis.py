import numpy as np

def set_fft(t,data):
	sp = np.fft.fft(data)
	t_max = np.amax(t)
	t_min = np.amin(t)
	t_t = t_max-t_min
	dt = t[1]-t[0]
	freq = np.fft.fftfreq(len(t),d=dt)
	freq = freq * 2*np.pi
	return freq,sp
def set_fft2(x,t,data):
	sp = np.fft.fft2(data)
	dt = t[1]-t[0]
	freq = np.fft.fftfreq(len(t),d=dt)
	freq = freq * 2*np.pi
	dx = x[1]-x[0]
	wave = np.fft.fftfreq(len(x),d=dx)
	wave = wave * 2*np.pi
	return wave,freq,sp