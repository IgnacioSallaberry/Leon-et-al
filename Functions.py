# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:00:04 2024

@author: Ignacio Sallaberry

"""

import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams["mathtext.fontset"] = "dejavusans" ## Aparencia default de la tipografia de matplotlib
plt.rcParams['font.family'] = 'Arial'  ## Biophysical Journal
plt.rcParams['mathtext.default'] = 'default'
from scipy.stats import sem


def PLOT_oligomeric_states(data, point_markers, point_colors, labels, width= 0.08, fig_width=3, fig_height=3, dpi=300, 
                           Y_lim=True, marker_size=10, labelpad = 2, lw=1, fontsize=12,
                           Xlabel='', Ylabel='', Title=''):
    '''
    

    Parameters
    ----------
    data : ndarray
        A = np.array([[data_first_plot], [data_second_plot], ...])
    
    point_markers : list of str
        Symbol for each data.
            Example: ['o' ,'*', '^', ...]
    
    point_colors : list of str
        Colors of each data.
            Example: ['r', 'g', 'b']
    
    labels : list of str
        xlabel of each data.
            Example: ['first plot', 'second plot', ...]
    
    width : float, optional
        Value for generate separation from central axis 
        and avoid superposition of data. 
        The default is 0.08.

    fig_width : float or int, optional
        The default is 3.

    fig_height : TYPE, optional
        The default is 3.

    dpi : int, optional
        Figure resolution. The default is 300.
        If dpi change may be necessary to adjutst other figures parameters
        (marker_size, fontsize, fig_width, fig_height) for better visualization.

    Y_lim : Bool , By default = True
        This is for visualization only.
        If not True, them Y_lim must be a list or ndarray of two components.
        
        If Y_lim = True:
            then y-axis lowest value is 95% of data 
            lowest value and y-axis upper value is 5% of highest data value
        
        If not Y_lim must be a list of floats = [minium y-axis value, maximum y-axis_value]
   
    marker_size : int, optional
        Size of markers. The default is 10.

    labelpad : float or int, optional
        Separation of label from axis. The default is 2.

    lw : float or int, optional
        width of mean and sem lines. The default is 1.
    
    fontsize : float or int, optional
        The default is 12.
    
    Xlabel : str, optional
        Label of x-axis of the figure.
    
    Ylabel : str, optional
        Label of y-axis of the figure.
        
    Title : str, optional
        Title of the figure.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    None.

    '''


    if len(data)>len(point_markers):
        raise ValueError ('Number of symbols is lower than number of data set to be plot')
        
    if len(data)<len(point_markers):
        raise ValueError ('Number of symbols is higher than number of data set to be plot')
                    
    if len(data)>len(point_colors):
        raise ValueError ('Number of colors is lower than number of data set to be plot')
        
    if len(data)<len(point_colors):
        raise ValueError ('Number of colors is higher than number of data set to be plot')
        
    if len(data)>len(labels):
        raise ValueError ('Numbers of labels is lower than number of data set to be plot')
        
    if len(data)<len(labels):
        raise ValueError ('Numbers of labels is higher than number of data set to be plot')
    
    if isinstance(Y_lim, (list, np.ndarray)):
        if np.asarray(Y_lim).ndim==1 and len(Y_lim)!=2:
            raise ValueError ('Y_lim must either True or list/ndarray with two elements')
        
    elif Y_lim==False:
        raise ValueError ('Y_lim must either True or list/ndarray with two elements')
                

    
    for d in range(len(data)):
        data[d] = list(data[d])
    #==============================================================================
    #                                Calculamos los cuartiles y la mediana
    #============================================================================== 

    ## Standard error of the mean = STD/sqrt(N) where N is the number of elements https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.sem.html
    SEM = []   
    ## obs: The scipy.stats.sem function uses a default value of ddof=1 for the number-of-degrees-of-freedom parameter while numpy.std uses ddof=0 by default.    
    means = []
    
    for i in range(len(data)):
        means.append(np.mean(data[i]))
        
        SEM.append(sem(data[i]))   
            
        
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
    
    Positions=list(np.arange(0,len(data)))
       
    #==============================================================================
    #                                Creamos los violin-plot
    #==============================================================================  

    from scipy.stats import gaussian_kde


    #==============================================================================
    #                                Randomnize values position in x-axis on each data set for better visualization.
    #                                effect may be control with "width" parameter
    #==============================================================================

    for i in range(1,len(data)+1):
        kde = gaussian_kde(data[i-1])
        density = kde(data[i-1])     # estimate the local density at each datapoint

    

            # generate some random jitter between 0 and 1
            # if jitter = 0 then values are align. Two or more equals values will not be distinguished
        jitter = np.random.rand(len(data[i-1])) - 0.5 
    
    
        # scale the jitter by the KDE estimate and add it to the centre x-coordinate
        xvals = i + (density * jitter * width * 2)
        plt.scatter(xvals, data[i-1], marker=point_markers[i-1], s=marker_size, c=point_colors[i-1])
    MAX=[]
    MIN=[]
    for d in data:
        MIN.append(min(d))
        MAX.append(max(d))

    #==============================================================================
    #                                plot mean and SEM lines
    #==============================================================================  

    for i in range(0,len(data)):
        plt.hlines(means[i]+SEM[i], 1+i-0.1, 1+i+0.1, linestyle='--', lw=lw, colors='k')
        plt.hlines(means[i], 1+i-0.1, 1+i+0.1, lw=lw, colors='k')
        plt.hlines(means[i]-SEM[i], 1+i-0.1, 1+i+0.1, linestyle='--', lw=lw, colors='k')

    


    plt.xticks(np.arange(1,len(data)+1), labels, fontsize=fontsize)
    if Y_lim==True:

        plt.ylim(min(MIN)*0.95,
                 max(MAX)*1.05)
    else:
        plt.ylim(Y_lim[0], Y_lim[1]*1.05)
    
    fig.subplots_adjust(top=0.985,
                        bottom=0.125,
                        left=0.230,
                        right=0.94,
                        hspace=0.2,
                        wspace=0.205)
    
    
    plt.xlabel(Xlabel, fontsize = fontsize)
    plt.ylabel(Ylabel, fontsize = fontsize, labelpad=15)
    plt.title(Title)
    
    ax.tick_params(which='minor', length=1.25, width=1)
    ax.tick_params(which='major', length=2.25, width=1)
    ax.tick_params(axis='both', labelsize=fontsize)

    plt.show()
