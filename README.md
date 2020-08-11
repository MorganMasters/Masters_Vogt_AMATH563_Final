# AMATH563 Final Project
## Modeling the Ferromagnetic Transition of the 2D Ising Model Using PDE-Find
### Morgan Masters, Ryan Vogt

Here, a friend and I attempted to build a model to fit the evolution of a complex, networked system through a transition which dramatically changes its behavior. The system in question is the 2D Ising spin model, which is a grid of interacting variables known to exhibit a transition from ordered to disordered structure at a particular temperature. This transition is driven by the interplay between a mutual ordering force (magnetic coupling) and a universal disordering force (thermal randomness); below a certain temperature, the ordering force prevails over the otherwise-dominant thermal disorder.

We approached the modeling problem from the standpoint of the singular value decomposition (SVD), which describes the number of important patterns in a particular set of data. Below the critical temperature, only one impoortant pattern exists: the one imposing order. Above that temperature, randomness prevails and there is no finite set of important patterns. Time did not allow for the conclusive work of finding a well-fitted model, but the full assembly of the pipeline was accomplished in 2 weeks and preliminary models were generated.

Practically, this demonstrates an ability to assess data collected across a range of conditions for dominant behaviors, as informed by optimization approaches, and subsequent analysis of that behavior according to the mathematical principles of the study of dynamical systems and differential equations.

In this project: 

- [x] Synthetic data was generated at evenly-spaced temperatures across the interval [0, 5] Kelvin.

    - Simulate thermodynamic equilibration of random initial state at each temperatuire via a Monte Carlo method to capture probabilistic behavior.
    
    - Equilibrate at a range of temperatures to model see thermodynamically-modulated behavior, such as ferromagnetic transition.
    
- [x] For each equilibration timestep (Monte Carlo iteration), rearrange grid state to vector and collect all timestep vectors into a state matrix.

- [x] Compute the SVD of the state matrix for each temperature.

- [x] Plot all singular values as a function of temperature and time (to see evolution with respect to both variables)

    - There is a sharp change in the distribution of singular values at the temperature corresponding to the known ferromagnetic transition temperature of the 2D Ising model.

- [x] Using PDE-Find (non-neural model-fitting algorithm), construct systems of differential equations which describes the dynamics. Subsequently, assess for bifurcation behavior.

- [ ] Identify a bifurcating differential system which matches the visible dynamics.

PDE-Find was developed by the research of Dr. Samuel Rudy (https://arxiv.org/pdf/1609.06401.pdf), a contemporary at UW AMATH.
