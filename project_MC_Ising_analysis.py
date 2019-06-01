#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import pywt
import scipy
import pickle

#%%

def load_config(file_path, grid_size, sample):
    file = open(file_path + "Ising" + str(grid_size) + "_" + str(sample) + ".pickle", 'rb')
    return pickle.load(file)

#%%  Initialize Parameters
nt      = 88         #  number of temperature points
N       = 4          #  size of the lattice, N x N

#%%  SVD on raw data

for i in range(1,2):

    file_path = "C:\\Users\Code\\repo\\"        
    df = load_config(file_path, 4, i)  # load data

    for data in df['State']:

        u,s,v=np.linalg.svd(data)
            
        plt.figure()
        plt.plot(u[:,0])

    title = 'Singular Value Spectrum ' + str(i) + ', '  + str(N) + 'x' + str(N)
    plt.title(title)

#%%
file_path = "C:\\Users\Code\\repo\\"        
df = load_config(file_path, 4, 1)  # load data
#%%

for i in range(3):
    u,s,v=np.linalg.svd(df.iloc[i][0])
            
    plt.figure(0, figsize=(15,15))
    plt.plot(v[:,0])    

    plt.figure(1, figsize=(15,15))
    plt.plot(v[:,1]) 

    plt.figure(2, figsize=(15,15))
    plt.plot(v[:,2]) 









#%%
keep = np.empty((nt,N*N))

for i in range(nt):
    u,s,v=np.linalg.svd(df.iloc[i][0])

    keep[i,:]=s

#%%

for i in range(nt):
    plt.figure()
    plt.plot(keep[i,:])
    plt.show()