import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def cplot(x,y,x_min,x_max,y_min,y_max,sym,color,ll,lb,thick,
          title,tfont,xtitle,xfont,ytitle,yfont,pox,poy,xpanel,ypanel,direct='in'):

    if ll == 0:
        all = False #'off'
    else:
        all = True #'on'

    if lb == 0:
        alb = False #'off'
    else:
        alb = True #'on'
		
    fig = plt.gcf()    
    ax = fig.add_axes([pox, poy, xpanel, ypanel])
    #plt.rc('text', usetex=True)
    #plt.rc('font', family='serif')
    plt.plot(x, y, sym, color=color, lw = thick)

    #font = FontProperties()
    #font.set_weight('bold')

    plt.xlim(x_min,x_max)
    plt.tick_params(
        axis='x',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        bottom=True,     # ticks along the bottom edge are off
        top=True,        # ticks along the top edge are off
        direction=direct,# Puts ticks inside the axes, outside the axes, or both
        labelbottom=alb) # labels along the bottom edge are off


    plt.ylim(y_min,y_max)
    plt.tick_params(
        axis='y',        # changes apply to the y-axis
        which='both',    # both major and minor ticks are affected
        left=True,       # ticks along the bottom edge are off
        right=True,      # ticks along the top edge are off
        direction=direct,# Puts ticks inside the axes, outside the axes, or both
        labelleft=all)   # labels along the left edge are off

    plt.minorticks_on()
    plt.title (title , fontsize=tfont)
    plt.xlabel(xtitle, fontsize=xfont)
    plt.ylabel(ytitle, fontsize=yfont)


def pltlogy(x,y,x_min,x_max,y_min,y_max,sym,color,ll,lb,thick,
            title,tfont,xtitle,xfont,ytitle,yfont,pox,poy,xpanel,ypanel,direct='in'):

    if ll == 0:
        all = False #'off'
    else:
        all = True #'on'

    if lb == 0:
        alb = False #'off'
    else:
        alb = True #'on'
		
    fig = plt.gcf()    
    ax = fig.add_axes([pox, poy, xpanel, ypanel])
    #plt.rc('text', usetex=True)
    #plt.rc('font', family='serif')
    plt.semilogy(x, y, sym, color=color, lw = thick)

    #font = FontProperties()
    #font.set_weight('bold')

    plt.xlim(x_min,x_max)
    plt.tick_params(
        axis='x',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        bottom=True,     # ticks along the bottom edge are off
        top=True,        # ticks along the top edge are off
        labelbottom=alb, # labels along the bottom edge are off
        direction=direct)# Puts ticks inside the axes, outside the axes, or both

    plt.ylim(y_min,y_max)
    plt.tick_params(
        axis='y',        # changes apply to the y-axis
        which='both',    # both major and minor ticks are affected
        left=True,       # ticks along the bottom edge are off
        right=True,      # ticks along the top edge are off
        labelleft=all,   # labels along the left edge are off
        direction=direct)# Puts ticks inside the axes, outside the axes, or both

    plt.minorticks_on()
    plt.title (title , fontsize=tfont)
    plt.xlabel(xtitle, fontsize=xfont)
    plt.ylabel(ytitle, fontsize=yfont)


def pltlogxy(x,y,x_min,x_max,y_min,y_max,sym,color,ll,lb,thick,
             title,tfont,xtitle,xfont,ytitle,yfont,pox,poy,xpanel,ypanel,direct='in'):

    if ll == 0:
        all = False #'off'
    else:
        all = True #'on'

    if lb == 0:
        alb = False #'off'
    else:
        alb = True #'on'
		
    fig = plt.gcf()    
    ax = fig.add_axes([pox, poy, xpanel, ypanel])
    #plt.rc('text', usetex=True)
    #plt.rc('font', family='serif')
    plt.loglog(x, y, sym, color=color, lw = thick)

    #font = FontProperties()
    #font.set_weight('bold')

    plt.xlim(x_min,x_max)
    plt.tick_params(
        axis='x',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        bottom=True,     # ticks along the bottom edge are off
        top=True,        # ticks along the top edge are off
        labelbottom=alb, # labels along the bottom edge are off
        direction=direct)# Puts ticks inside the axes, outside the axes, or both

    plt.ylim(y_min,y_max)
    plt.tick_params(
        axis='y',        # changes apply to the y-axis
        which='both',    # both major and minor ticks are affected
        left=True,       # ticks along the bottom edge are off
        right=True,      # ticks along the top edge are off
        labelleft=all,   # labels along the left edge are off
        direction=direct)# Puts ticks inside the axes, outside the axes, or both

    plt.minorticks_on()
    plt.title (title , fontsize=tfont)
    plt.xlabel(xtitle, fontsize=xfont)
    plt.ylabel(ytitle, fontsize=yfont)