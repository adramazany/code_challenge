import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random as ran
import math 
path = '/'
## function to read input data
def read_data(filname):
    params = {}
    with open(filname) as fil:
        lines = fil.readlines()
        for line in lines:
            line= line.split("=")
            #if  line[0].strip() == 'rho':
                #params[line[0].strip()] = [float(v) for v in line[1].split(",")]
            #else:
            params[line[0].strip()] = float(line[1])
            
   
    print(f"Input parameters defined: {params}")
    return params
## function to define an initial configuration of particles
def initial_config():
    rx, ry, rz = np.zeros(N), np.zeros(N), np.zeros(N)
    rx[0] = ran.random()*Lx
    ry[0] = ran.random()*Ly
    rz[0] = ran.random()*Lz
    for i in range(1,N):
        flag = 1
        while (flag == 1):
            flag = 0
            rx[i] = ran.random()*Lx
            ry[i] = ran.random()*Ly
            rz[i] = ran.random()*Lz
            for j in range(i):
                rxd = rx[j] - rx[i]
                ryd = ry[j] - ry[i]
                rzd = rz[j] - rz[i]
                rxd = rxd - np.round(rxd/Lx)*Lx  ## minimum image 
                ryd = ryd - np.round(ryd/Ly)*Ly
                rzd = rzd - np.round(rzd/Lz)*Lz
                dsq = rxd*rxd + ryd*ryd + rzd*rzd
                if dsq < ovrlap: 
                    flag = 1
# find the mininum distance once all the particles are inserted.. using nested for loops
    dmin = Lx*Lx
    for i in range(N-1):
        for j in range(i+1,N):
            rxd = rx[j] - rx[i]
            ryd = ry[j] - ry[i]
            rzd = rz[j] - rz[i]
            rxd = rxd - np.round(rxd/Lx)*Lx  ## minimum image 
            ryd = ryd - np.round(ryd/Ly)*Ly
            rzd = rzd - np.round(rzd/Lz)*Lz
            dsq = rxd*rxd + ryd*ryd + rzd*rzd
            dmin = min(dmin, dsq)
    dmin = dmin**0.5
    if (dmin < ovrlap): 
        print(f'Particles overlap, min distance = {np.round(dmin, decimals = 3)}')
    else:
        print(f'Particles do not overlap, min distance = {np.round(dmin, decimals = 3)}')
    return rx, ry, rz        
## initialize variables
def initialize_parameters(params):
    sig = params['sigma']
    eps = params['epsilon']
    m = params['m']
    Lx = params['Lx']
    Ly = params['Ly']
    Lz = params['Lz']
    N = int(params['N'])
    ovrlap = params['ovrlap']**2
    rho = params['rho']
    monte_carlo_steps = np.int64(params['monte_carlo_steps'])
    rcutsq = params['rcut']*sig
    rcutsq = rcutsq*rcutsq
    sig6 = sig*sig*sig
    sig6 = sig6*sig6
    sig12 = sig6*sig6
    T = params['T']
    P = params['P']
    vol= N/rho
    delta_d=params['delta_d']
    
    print(f'Number of particles are {N}')
    return sig, eps, m, Lx, Ly, Lz, N, ovrlap, rho, monte_carlo_steps, rcutsq, sig6, sig12, T, P, vol, delta_d
### Monte Carlo calculation
def monte_carlo(rx, ry, rz):
    U = 0
    for i in range(N-1):
        for j in range(i+1,N):
            rxd = rx[i] - rx[j]
            ryd = ry[i] - ry[j]
            rzd = rz[i] - rz[j]
            rxd = rxd - np.round(rxd/Lx)*Lx
            ryd = ryd - np.round(ryd/Ly)*Ly
            rzd = rzd - np.round(rzd/Lz)*Lz
            dsq = rxd*rxd + ryd*ryd + rzd*rzd
            if (dsq < rcutsq):
                U = U + sig12/(dsq**6)-sig6/(dsq**3)
                
    U = 4*eps*U
    return  U
def calc_monte_carlo():
    
    PE = np.zeros(monte_carlo_steps)
    acceptance = np.zeros(monte_carlo_steps)

    rx, ry, rz = initial_config()
    U = monte_carlo(rx, ry, rz)
    PE[0] = U
    acceptance[0]=1
   
    for i in range(1, monte_carlo_steps):
        print (f"Progress:  {((i/monte_carlo_steps)*100):4.1f}%", end = '\r')
        n_rx, n_ry, n_rz = position_integration(rx, ry, rz)
        print(rx[0])
        U = monte_carlo (rx,ry,rz)
        PE[i] = U
        if PE[i] < PE[i-1]:
            acceptance[i]=1
            rx, ry, rz = n_rx, n_ry, n_rz
        else:
            acceptance[i]=0

    return PE, acceptance


# In[93]:


def position_integration(rx, ry, rz):
    # rx = rx + (delta_d * ((2*ran.random())-1))
    # ry = ry + (delta_d * ((2*ran.random())-1))
    # rz = rz + (delta_d * ((2*ran.random())-1))
    for i in range(N):
        rx[i] = rx[i] + (delta_d * ((2*ran.random())-1))
        ry[i] = ry[i] + (delta_d * ((2*ran.random())-1))
        rz[i] = rz[i] + (delta_d * ((2*ran.random())-1))
    return rx, ry, rz     

### read input file ###

inputfil = 'params.MC.in'
params = read_data(inputfil)  
##### Initialize parameters 
sig, eps, m, Lx, Ly, Lz, N, ovrlap, rho, monte_carlo_steps, rcutsq, sig6, sig12, T, P, vol, delta_d = initialize_parameters(params)

PE , acceptance = calc_monte_carlo()
print ('PE=', PE, 'acceptance=',acceptance)


# In[ ]:




