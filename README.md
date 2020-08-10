# AMATH563 Final Project
## Modeling the Ferromagnetic Transition of the 2D Ising Model Using PDE-Find
### Morgan Masters, Ryan Vogt

In this project: 

- [x] Synthetic data was generated at evenly-spaced temperatures across [0, 5] Kelvin ([-273.15, -268.15] degrees Celcius) interval.

    - Simulate thermodynamic equilibration of random initial state at each temperatuire via a Monte Carlo method to capture probabilistic behavior.
    
    - Equilibrate at a range of temperatures to model see thermodynamically-modulated behavior, such as ferromagnetic transition.
    
- [x] For each equilibration timestep (Monte Carlo iteration), rearrange grid state to vector and collect all timestep vectors into matrix.

- [x] Compute the singular value decomposition (SVD) of the state matrix for each temperature.

- [x] Plot all singular values as a function of temperature and time (to see evolution w.r.t. both variables)

    - There is a sharp change in the distribution of singular values at the temperature corresponding to the known ferromagnetic transition temperature of the 2D Ising model.

- [x] Using PDE-Find (non-neural model-fitting algorithm), construct systems of differential equations which describes the dynamics. Subsequently, assess for bifurcation behavior.

- [ ] Identify a bifurcating differential system which matches the visible dynamics.

PDE-Find was developed by the research of Dr. Samuel Rudy (https://arxiv.org/pdf/1609.06401.pdf), a contemporary at UW AMATH.
