#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from scipy.sparse import diags

from sklearn import linear_model
from sklearn.model_selection import train_test_split

#%% Define functions for analysis

def STRidge(library, dynamics, alpha, tol, iters=1000):  

    thresh = tol * np.ones(library.shape[0])
    lib_ind = [range
    for i in range(iter):

        reg = linear_model.Ridge(alpha=alpha)  # regress
        mod = reg.fit(library,time_deriv)
        xi = mod.coef_

        for j in range(length(xi)):

            if coef < tol:  # threshold out small coefficients
                library_new = np.delete(library,library[:,j])

            j += 1

        if library_new == library:  # check to exit
            break
        else:
            library = library_new

    return xi


def PDE_Find(library, dynamics, xi_best, error_best, d_tol, tol_iters):
  
  library_train, library_test, dynamics_train, dynamics_test = train_test_split(library, dynamics, test_size=1/5)

    tol = d_tol
    alpha = 1e-3 * np.linalg.cond(library)

  for iter in range(tol_iters):
    xi = STRidge(library=library_train, dynamics=dynamics_train, alpha=alpha, tol=tol)
    error = np.linalg.norm(np.matmul(library_test, xi) - dynamics_test)**2 + alpha * np.linalg.norm(xi,0)

    if error <= error:
      xi_best = xi
      error_best = error
      tol += d_tol
    else:
      tol = max([0, tol - 2 * d_tol])
      d_tol = 2 * d_tol / (tol_iters - iter)
      tol += d_tol
  return xi_best, error_best




# compute dynamics
def calc_dyn(data, h):
    length = data.shape[0] 
    A = 1 / (2 * h) * diags([-1, 0, 1], [-1, 0, 1], shape=(length, length)).todense()
    dynamics = np.matmul(A, data[:,:])[1:-1, :] # neglect first and last entry per temperature axis to avoid boundary conflicts with cetnral differencing
    return dynamics

def build_library(data, temps, degree=3):
    t = [np.array(temps[1:-1])]
    ts = np.repeat(t, np.shape(data)[1], axis = 0).T
    data = data.flatten()
    ts = ts.flatten()
    library = np.zeros([len(ts), 0])
    
    for i in range(degree+1):
        for j in range(i+1):
            library = np.append(library, np.expand_dims((data**j)*(ts**(i-j)), -1), axis = 1)
    return library
    
#%% Main algorithm 

# get baseline xi and error
# xi_best =  # inverse of training library times training dynamics
# error_best =  # compute value of ridge regression cost function for xi_best, using test sets, given alpha = 1e-3 * np.linalg.cond(library) 

# # apply PDE_Find
# d_tol = 0.01
# tol_iters = 100

# xi_best, error_best = PDE_Find(library=library, dynamics=dynamics, xi_best=xi_best, error_best=error_best, d_tol=d_tol, tol_iters=tol_iters)    

# #%%
