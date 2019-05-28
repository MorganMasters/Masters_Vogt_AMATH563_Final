#%%
from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

from numpy.random import rand

from pprint import pprint

#%% BLOCK OF FUNCTIONS USED IN THE MAIN CODE

def initialstate(N):   
    ''' generates a random spin configuration for initial condition'''
    state = 2*np.random.randint(2, size=(N,N))-1
    return state

def mcmove(config, beta):
    '''Monte Carlo move using Metropolis algorithm '''
    for i in range(N):
        for j in range(N):
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s =  config[a, b]
                nb = config[(a+1)%N,b] + config[a,(b+1)%N] + config[(a-1)%N,b] + config[a,(b-1)%N]
                cost = 2*s*nb
                if cost < 0:
                    s *= -1
                elif rand() < np.exp(-cost*beta):
                    s *= -1
                config[a, b] = s
    return config

#%% change these parameters for a smaller (faster) simulation 

nt      = 88         #  number of temperature points
N       = 32         #  size of the lattice, N x N
eqSteps = 1024       #  number of MC sweeps for equilibration
mcSteps = 1024       #  number of MC sweeps for calculation

T = np.linspace(1.53, 3.28, nt)
E,M,C,X = np.zeros(nt), np.zeros(nt), np.zeros(nt), np.zeros(nt)
n1, n2  = 1.0/(mcSteps*N*N), 1.0/(mcSteps*mcSteps*N*N) 
# divide by number of samples, and by system size to get intensive values

#%% MAIN PART OF THE CODE
data=list()

for i in range(1,11):
        
    for tt in range(nt):
     #   E1 = M1 = E2 = M2 = 0
        config = initialstate(N)         # initialize random configuration
        iT=1.0/T[tt]; iT2=iT*iT

        for j in range(eqSteps):         
            mcmove(config, iT)           # equilibrate
            data.append([config,T[tt]])  # keep config/temperature
    
    df=pd.DataFrame(data,columns=['config','temp'])

    x='Ising32_' + str(i) + '.pickle'

    with open(x, 'wb') as f:
        pickle.dump(df, f)