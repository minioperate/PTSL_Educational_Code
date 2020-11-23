# color level plot using imshow
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import sys, os
dir = '/media/tctsai/work-SSD/python_lib'  # for linux
#dir = "D:\Work\program\python\lib" # for windows


#------------------------------------------------------------------------------------
def custom_color(color,level):
#   color = 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', ......
#     http://matplotlib.org/users/colormaps.html
#   level = 0~255
#
    NCURVES = 256
    values = range(NCURVES)
    jet = cm = plt.get_cmap(color) 
    cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
    colorVal = scalarMap.to_rgba(values[level])
    return colorVal


#------------------------------------------------------------------------------------
def colorplot(data,cbmin,cbmax,x_min,x_max,y_min,y_max,cmap,itpl,
              title,xtitle,ytitle,cbtitle,xfigsize,yfigsize,pox,poy,xpanel,ypanel):
#  itpl = interploation mode
#  Acceptable values are 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 
#    'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 
#    'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'
#  cmap = color map
  
    fig = plt.gcf()    
    ax = fig.add_axes([pox, poy, xpanel, ypanel])

#    data = np.flipud(data)  # Don't use this command when using pcolormesh 
    asp = yfigsize*ypanel*(x_max-x_min)/(xfigsize*xpanel*(y_max-y_min))

    ax.set_title(title)
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)

    plt.axis([x_min, x_max, y_min, y_max])

    im = plt.imshow(data, cmap=cmap, vmin=cbmin, vmax=cbmax, origin='lower',
                    extent=[x_min, x_max, y_min,y_max], aspect=asp, interpolation=itpl) #, zorder=1)

#  plot color bar
    cbpox = pox+xpanel+0.02*xpanel
    cbpoy = poy
    cbxpanel = 0.025*xpanel
    cbypanel = ypanel

    cb = fig.add_axes([cbpox,cbpoy,cbxpanel,cbypanel])
    cbar = plt.colorbar(im, cax=cb)
    cbar.ax.set_ylabel(cbtitle)
    plt.sca(ax)


#------------------------------------------------------------------------------------
def cbcontourf(x,y,data,cmap,ll,lb,levels,cb_title,ttsize,
               xfigsize,yfigsize,pox,poy,xpanel,ypanel,cbpox,cbpoy,cbxpanel,cbypanel,
               direct='out',extends='both'):
#
#  Acceptable values are 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 
#    'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 
#    'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'
#  cmap = color map
#
    if ll == 0:
        all = 'off'
    else:
        all = 'on'

    if lb == 0:
        alb = 'off'
    else:
        alb = 'on'

    fig = plt.gcf()    
    ax = fig.add_axes([pox, poy, xpanel, ypanel]) 
    cs = plt.contourf(x, y, data, levels, cmap=cmap, extend=extends, origin='lower')

    #plt.xlim(x_min,x_max)
    plt.tick_params(
        axis='x',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        bottom='on',     # ticks along the bottom edge are off
        top='on',        # ticks along the top edge are off
        direction=direct,# Puts ticks inside the axes, outside the axes, or both
        labelbottom=alb) # labels along the bottom edge are off

    #plt.ylim(y_min,y_max)
    plt.tick_params(
        axis='y',        # changes apply to the y-axis
        which='both',    # both major and minor ticks are affected
        left='on',       # ticks along the bottom edge are off
        right='on',      # ticks along the top edge are off
        direction=direct,# Puts ticks inside the axes, outside the axes, or both
        labelleft=all)   # labels along the left edge are off

    plt.minorticks_on()
    cb = fig.add_axes([cbpox,cbpoy,cbxpanel,cbypanel])
    cbar = plt.colorbar(cs, cax=cb)
    cbar.ax.set_ylabel(cb_title, fontsize=ttsize, fontweight='bold')
    plt.sca(ax)


#------------------------------------------------------------------------------------
def cpimshow(data,cbmin,cbmax,x_min,x_max,y_min,y_max,cmap,itpl,ll,lb,
             xfigsize,yfigsize,pox,poy,xpanel,ypanel,direct='out'):
#  itpl = interploation mode
#  Acceptable values are 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 
#    'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 
#    'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'
#  cmap = color map
			  
    if ll == 0:
        all = 'off'
    else:
        all = 'on'

    if lb == 0:
        alb = 'off'
    else:
        alb = 'on'

    fig = plt.gcf()    
    ax = fig.add_axes([pox, poy, xpanel, ypanel]) 
    asp = yfigsize*ypanel*(x_max-x_min)/(xfigsize*xpanel*(y_max-y_min))
    #plt.axis('off')
    im = plt.imshow(data, cmap=cmap, vmin=cbmin, vmax=cbmax, origin='lower',aspect=asp, interpolation=itpl,
                    extent=[x_min, x_max, y_min,y_max])

    plt.xlim(x_min,x_max)
    plt.tick_params(
        axis='x',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        bottom='on',     # ticks along the bottom edge are off
        top='on',        # ticks along the top edge are off
        direction=direct,# Puts ticks inside the axes, outside the axes, or both
        labelbottom=alb) # labels along the bottom edge are off

    plt.ylim(y_min,y_max)
    plt.tick_params(
        axis='y',        # changes apply to the y-axis
        which='both',    # both major and minor ticks are affected
        left='on',       # ticks along the bottom edge are off
        right='on',      # ticks along the top edge are off
        direction=direct,# Puts ticks inside the axes, outside the axes, or both
        labelleft=all)   # labels along the left edge are off

    plt.minorticks_on()



#------------------------------------------------------------------------------------
def cbimshow(data,cbmin,cbmax,x_min,x_max,y_min,y_max,cmap,itpl,ll,lb,cbticks,
             xfigsize,yfigsize,pox,poy,xpanel,ypanel,cbpox,cbpoy,cbxpanel,cbypanel,direct='out',cbtitle='',fonts=20):
#  itpl = interploation mode
#  Acceptable values are 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 
#    'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 
#    'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'
#  cmap = color map

    if ll == 0:
        all = 'off'
    else:
        all = 'on'

    if lb == 0:
        alb = 'off'
    else:
        alb = 'on'

    fig = plt.gcf()    
    ax = fig.add_axes([pox, poy, xpanel, ypanel]) 
    asp = yfigsize*ypanel*(x_max-x_min)/(xfigsize*xpanel*(y_max-y_min))
    #plt.axis('off')
    im = plt.imshow(data, cmap=cmap, vmin=cbmin, vmax=cbmax, origin='lower',aspect=asp, interpolation=itpl,
                    extent=[x_min, x_max, y_min,y_max])

    plt.xlim(x_min,x_max)
    plt.tick_params(
        axis='x',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        bottom='on',     # ticks along the bottom edge are off
        top='on',        # ticks along the top edge are off
        direction=direct,# Puts ticks inside the axes, outside the axes, or both
        labelbottom=alb) # labels along the bottom edge are off

    plt.ylim(y_min,y_max)
    plt.tick_params(
        axis='y',        # changes apply to the y-axis
        which='both',    # both major and minor ticks are affected
        left='on',       # ticks along the bottom edge are off
        right='on',      # ticks along the top edge are off
        direction=direct,# Puts ticks inside the axes, outside the axes, or both
        labelleft=all)   # labels along the left edge are off

    plt.minorticks_on()

    #  plot color bar
    cb = fig.add_axes([cbpox,cbpoy,cbxpanel,cbypanel])
    cbar = plt.colorbar(im, cax=cb, ticks=cbticks)
    cbar.ax.set_ylabel(cbtitle, fontsize=fonts, fontweight='bold')
    plt.sca(ax)
    #ax = fig.add_axes([pox, poy, xpanel, ypanel])



#------------------------------------------------------------------------------------
def colorplot_invert_y(data,cbmin,cbmax,x_min,x_max,y_min,y_max,cmap,itpl,
              title,xtitle,ytitle,cbtitle,xfigsize,yfigsize,pox,poy,xpanel,ypanel):
#  itpl = interploation mode
#  Acceptable values are ‘none’, ‘nearest’, ‘bilinear’, ‘bicubic’, ‘spline16’, 
#    ‘spline36’, ‘hanning’, ‘hamming’, ‘hermite’, ‘kaiser’, ‘quadric’, ‘catrom’, 
#    ‘gaussian’, ‘bessel’, ‘mitchell’, ‘sinc’, ‘lanczos’
#  cmap = color map
			  
    fig = plt.gcf()    
    ax = fig.add_axes([pox, poy, xpanel, ypanel])

#    data = np.flipud(data)  # Don't use this command when using pcolormesh 
    asp = yfigsize*ypanel*(x_max-x_min)/(xfigsize*xpanel*(y_max-y_min))

    ax.set_title(title)
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)
	
    plt.axis([x_min, x_max, y_max, y_min])
	
    im = plt.imshow(data, cmap=cmap, vmin=cbmin, vmax=cbmax, origin='upper',
                    extent=[x_min, x_max, y_max,y_min], aspect=asp, interpolation=itpl) #, zorder=1)

#  plot color bar
    cbpox = pox+xpanel+0.02*xpanel
    cbpoy = poy
    cbxpanel = 0.025*xpanel
    cbypanel = ypanel

    cb = fig.add_axes([cbpox,cbpoy,cbxpanel,cbypanel])
    cbar = plt.colorbar(im, cax=cb)
    cbar.ax.set_ylabel(cbtitle)


	
#------------------------------------------------------------------------------------
def make_cmap(colors, position=None, bit=False):
    '''
    make_cmap takes a list of tuples which contain RGB values. The RGB
    values may either be in 8-bit [0 to 255] (in which bit must be set to
    True when called) or arithmetic [0 to 1] (default). make_cmap returns
    a cmap with equally spaced colors.
    Arrange your tuples so that the first color is the lowest value for the
    colorbar and the last is the highest.
    position contains values from 0 to 1 to dictate the location of each color.
    '''
    import matplotlib as mpl
    import numpy as np
    bit_rgb = np.linspace(0,1,256)
    if position == None:
        position = np.linspace(0,1,len(colors))
    else:
        if len(position) != len(colors):
            sys.exit("position length must be the same as colors")
        elif position[0] != 0 or position[-1] != 1:
            sys.exit("position must start with 0 and end with 1")
    if bit:
        for i in range(len(colors)):
            colors[i] = (bit_rgb[colors[i][0]],
                         bit_rgb[colors[i][1]],
                         bit_rgb[colors[i][2]])
    cdict = {'red':[], 'green':[], 'blue':[]}
    for pos, color in zip(position, colors):
        cdict['red'].append((pos, color[0], color[0]))
        cdict['green'].append((pos, color[1], color[1]))
        cdict['blue'].append((pos, color[2], color[2]))

    cmap = mpl.colors.LinearSegmentedColormap('my_colormap',cdict,256)
    return cmap

#------------------------------------------------------------------------------------
def make_reds():
    #-- create a colors map -----------
    colors = [(255,255,255)]
    for i in range(1, 256, 1):
        colors.append((255,255,255))
    #print(colors)
    #----------------------------------
    iR = 255
    iG = 255
    iB = 255
    for i in range(1, 256, 1):
        #print(i)
        iG = iG-4
        if iG >= 0:
            colors[i] = (255, iG, 255)
        else:
            iB = iB-4
            if iB >=0:
                colors[i] = (255, 0, iB)
            else:
                iR = iR-1
                colors[i] = (iR, 0, 0)
    cmap = make_cmap(colors, bit=True)
    return cmap

	
#------------------------------------------------------------------------------------
def make_IDLCB37():
    #-- create a colors map -----------
    CB37 = np.load(dir+'/IDLCB37.npz')
    R = CB37['R37']
    G = CB37['G37']
    B = CB37['B37']
    colors = [(R[0], G[0], B[0])]
    for i in range(1, 256, 1):
        colors.append((R[i], G[i], B[i]))
    cmap = make_cmap(colors, bit=True)
    return cmap


#------------------------------------------------------------------------------------
def make_redblue(min,max):
    #-- create a colors map -----------
    colors = [(255,255,255)]
    for i in range(1, 256, 1):
        colors.append((255,255,255))
    #print(colors)
    #----------------------------------
    #  find the position of zero
    if min*max > 0:
        print('min*max >=0')
        print('Please check your setting !')
        print('Program STOP at make_redblue')
        exit()
    if min > max:
        print('min > max ?')
        print('Please check your setting !')
        print('Program STOP at make_redblue')
        exit()
    num_zero = int(256*abs(min)/(max+abs(min)))
    num_zero1 = num_zero+1
    #  color map for > 0
    iR = 255
    iG = 255
    iB = 255
    for i in range(num_zero1+1, 256, 1):
        #print(i)
        iG = iG-6
        if iG >= 0:
            colors[i] = (255, iG, 255)
        else:
            iB = iB-6
            if iB >=0:
                colors[i] = (255, 0, iB)
            else:
                iR = iR-1
                colors[i] = (iR, 0, 0)
    #  color map for < 0
    iR = 255
    iG = 255
    iB = 255
    for i in range(num_zero-1, -1, -1):
        #print(i)
        iR = iR-6
        if iR >= 0:
            colors[i] = (iR, 255, 255)
        else:
            iG = iG-6
            if iG >=0:
                colors[i] = (0, iG, 255)
            else:
                iB = iB-1
                colors[i] = (0, 0, iB)
    cmap = make_cmap(colors, bit=True)
    return cmap