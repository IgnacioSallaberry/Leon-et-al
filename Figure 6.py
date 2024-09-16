# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:42:27 2024

@author: Ignacio Sallaberry
"""

from os import getcwd, chdir
# wd=getcwd()
# chdir(wd)

# import os
# os.path.realpath(__file__)

import pandas as pd
try:
    from Functions import *
    path = getcwd()

except:
    import sys
    path = input ('Please copy and paste here the downloaded folder location:\n')
    # sys.path.append(path)
    chdir(path)
    from Functions import *


# read text file into pandas DataFrame
data = pd.read_csv(path+'\Epsilon_values.txt', sep="\t")
## Names of the columns
list(data.columns)

# display DataFrame
print(data)

Epsilon_mRFP = np.array(data['mRFP'].dropna().tolist()).ravel()

Epsilon_GPM6a = np.array(data['GPM6a'].dropna().tolist()).ravel()

Epsilon_T_71_P = np.array(data['T71P'].dropna().tolist()).ravel()

Epsilon_GPM6a_1 = np.array(data['GPM6a.1'].dropna().tolist()).ravel()

Epsilon_T_76_I = np.array(data['T76I'].dropna().tolist()).ravel()

Epsilon_GPM6a_2 = np.array(data['GPM6a.2'].dropna().tolist()).ravel()

Epsilon_T_210_N = np.array(data['T210N'].dropna().tolist()).ravel()

Epsilon_GPM6a_3 = np.array(data['GPM6a.3'].dropna().tolist()).ravel()

Epsilon_M_154_V = np.array(data['M154V'].dropna().tolist()).ravel()

Epsilon_F_156_Y = np.array(data['F156Y'].dropna().tolist()).ravel()
 
Epsilon_GPM6a_4 = np.array(data['GPM6a.4'].dropna().tolist()).ravel()

Epsilon_R_163_Q = np.array(data['R163Q'].dropna().tolist()).ravel()
   


#%%
####
##     mRFP vs M6a
####

labels_ = [r'$\frac{\varepsilon_{mRFP}}{<\epsilon_{mRFP}>}$',
           r'$\frac{\epsilon_{GPM6a}}{<\epsilon_{mRFP}>}$']

point_markers_ = ['o', 'o']
point_colors_ = ['r', r'#000080ff']

data = [list(Epsilon_mRFP/np.mean(Epsilon_mRFP)), 
        list(Epsilon_GPM6a/np.mean(Epsilon_mRFP))]
        
PLOT_oligomeric_states(data, point_markers_, point_colors_, labels_, Y_lim=[0,3.1], Ylabel=r'$\epsilon$')

#%%
####
##     M6a vs T71P
####

labels_ = [r'$\frac{\epsilon_{GPM6a}}{<\epsilon_{GPM6a}>}$',
           r'$\frac{\epsilon_{T71P}}{<\epsilon_{GPM6a}>}$']

point_markers_ = ['o', 'o']
point_colors_ = [r'#000080ff', r'#7e2954ff']

data = [list(Epsilon_GPM6a/np.mean(Epsilon_GPM6a)),
        list(Epsilon_T_71_P/np.mean(Epsilon_GPM6a))]

PLOT_oligomeric_states(data, point_markers_, point_colors_, labels_, Y_lim=[0,3.1], Ylabel=r'$\epsilon$')


#%%
####
##     M6a vs T76I
####

labels_ = [r'$\frac{\epsilon_{GPM6a}}{<\epsilon_{GPM6a}>}$',
           r'$\frac{\epsilon_{T76I}}{<\epsilon_{GPM6a}>}$']

point_markers_ = ['o', 'o']
point_colors_ = [r'#000080ff', r'#7e2954ff']

data = [list(Epsilon_GPM6a_1/np.mean(Epsilon_GPM6a_1)),
        list(Epsilon_T_76_I/np.mean(Epsilon_GPM6a_1))]

PLOT_oligomeric_states(data, point_markers_, point_colors_, labels_, Y_lim=[0,3.1], Ylabel=r'$\epsilon$')


#%%
####
##     M6a vs M154V
####

labels_ = [r'$\frac{\epsilon_{GPM6a}}{<\epsilon_{GPM6a}>}$',
           r'$\frac{\epsilon_{M154V}}{<\epsilon_{GPM6a}>}$']

point_markers_ = ['o', 'o']
point_colors_ = [r'#000080ff', r'#7e2954ff']


data = [list(Epsilon_GPM6a_3/np.mean(Epsilon_GPM6a_3)),
        list(Epsilon_M_154_V/np.mean(Epsilon_GPM6a_3))]

PLOT_oligomeric_states(data, point_markers_, point_colors_, labels_, Y_lim=[0,3.1], Ylabel=r'$\epsilon$')



#%%
####
##     M6a vs T210N
####

labels_ = [r'$\frac{\epsilon_{GPM6a}}{<\epsilon_{GPM6a}>}$',
           r'$\frac{\epsilon_{T210N}}{<\epsilon_{GPM6a}>}$']

point_markers_ = ['o', 'o']
point_colors_ = [r'#000080ff', r'#7e2954ff']


data = [list(Epsilon_GPM6a_2/np.mean(Epsilon_GPM6a_2)),
        list(Epsilon_T_210_N/np.mean(Epsilon_GPM6a_2))]

        
PLOT_oligomeric_states(data, point_markers_, point_colors_, labels_, Y_lim=[0,3.1], Ylabel=r'$\epsilon$')

#%%
####
##     M6a vs R163Q
####

labels_ = [r'$\frac{\epsilon_{GPM6a}}{<\epsilon_{GPM6a}>}$',
           r'$\frac{\epsilon_{R163Q}}{<\epsilon_{GPM6a}>}$']

point_markers_ = ['o', 'o']
point_colors_ = [r'#000080ff', r'#7e2954ff']


data = [list(Epsilon_GPM6a_4/np.mean(Epsilon_GPM6a_4)),
        list(Epsilon_R_163_Q/np.mean(Epsilon_GPM6a_4))]

        
PLOT_oligomeric_states(data, point_markers_, point_colors_, labels_, Y_lim=[0,3.1], Ylabel=r'$\epsilon$')

#%%
####
##     M6a vs F156Y
####

labels_ = [r'$\frac{\epsilon_{GPM6a}}{<\epsilon_{GPM6a}>}$',
           r'$\frac{\epsilon_{F156Y}}{<\epsilon_{GPM6a}>}$']

point_markers_ = ['o', 'o']
point_colors_ = [r'#000080ff', r'#7e2954ff']


data = [list(Epsilon_GPM6a_3/np.mean(Epsilon_GPM6a_3)),
        list(Epsilon_F_156_Y/np.mean(Epsilon_GPM6a_3))]

        
PLOT_oligomeric_states(data, point_markers_, point_colors_, labels_, Y_lim=[0,3.1], Ylabel=r'$\epsilon$')

