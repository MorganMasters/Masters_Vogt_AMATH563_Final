#%%
from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import scipy
import pickle

from numpy.random import rand

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

nt      = 200         #  number of temperature points
N       = 8          #  size of the lattice, N x N
eqSteps = 1024       #  number of MC sweeps for equilibration

T = np.linspace(0.05, 5.05, nt)            # pick between 1.53 and 3.28
#%% MAIN PART OF THE CODE

for j in range(1,11):  # simulate 10 experiments
    
    df = pd.DataFrame(columns=['State','Temperature'], index=range(nt))
    
    for tt in range(nt):  # equilibrate one configuration per temperature step
    
        config = initialstate(N)
        state = np.reshape(config,(1,N*N))

        iT=1.0 / T[tt]
    
        for i in range(1,eqSteps):  # equilibrate
            mcmove(config, iT)
            state = np.vstack((state, np.reshape(config,(1,N*N))))
            
        df.iloc[tt][0] = state
        df.iloc[tt][1] = T[tt]

        #plt.figure()
        #plt.imshow(state, aspect='auto')
        #plt.xlabel('Lattice Site')
        #plt.ylabel('Time')
        #plt.show()

    x='Ising_broad_' + str(N) + '_' + str(j) + '.pickle'
    
    with open(x, 'wb') as f:
        pickle.dump(df, f)    

#%%
