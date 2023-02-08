#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random as ran
import math

#%%

path = '/'

#%%

## function to read input data
def read_data(filname):
    params = {}
    with open(filname) as fil:
        lines = fil.readlines()
        for line in lines:
            line= line.split("=")
            if  line[0].strip() == 'rho':
                params[line[0].strip()] = [float(v) for v in line[1].split(",")]
            else:
                params[line[0].strip()] = float(line[1])


    print(f"Input parameters defined: {params}")
    return params

#%%

read_data("params.a2.in")

#%%

## function to define an initial configuration of particles
def initial_config():
    rx, ry, rz = np.zeros(N), np.zeros(N), np.zeros(N)
    Vx, Vy, Vz = np.zeros(N), np.zeros(N), np.zeros(N)
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
    return rx, ry, rz, Vx, Vy, Vz


#%%

## initialize variables
def initialize_parameters(params):
    sig = params['sigma']
    eps = params['epsilon']
    m = params['m']
    N = int(params['N'])
    ovrlap = params['ovrlap']**2
    rho_ar = params['rho']
    dt = params['dt']
    Nsteps = np.int64(params['Nsteps'])
    rcutsq = params['rcut']*sig
    rcutsq = rcutsq*rcutsq
    sig6 = sig*sig*sig
    sig6 = sig6*sig6
    sig12 = sig6*sig6
    T = params['T']
    rho_ar = np.array(rho_ar)
    vol_ar = N/rho_ar
    print("vol_ar=", vol_ar)
    Lx_ar = np.cbrt(vol_ar)
    Ly_ar = np.cbrt(vol_ar)
    Lz_ar = np.cbrt(vol_ar)
    print(f'Number of particles are {N}')
    return sig, eps, m, ovrlap, rho_ar, dt, Nsteps, rcutsq, N, sig6, sig12, T, vol_ar, Lx_ar, Ly_ar, Lz_ar

#%%

### force calculation
def force(rx, ry, rz, Vx, Vy, Vz):
    Fx, Fy, Fz = np.zeros(N), np.zeros(N), np.zeros(N)
    U = 0
    virial = 0
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
                f = 1/dsq*(2*sig12/(dsq**6)-sig6/(dsq**3))
                f2=(24*eps)*f*dsq
                virial+=f2
                fx = f*rxd
                fy = f*ryd
                fz = f*rzd
                Fx[i] = Fx[i] + fx
                Fy[i] = Fy[i] + fy
                Fz[i] = Fz[i] + fz
                Fx[j] = Fx[j] - fx  ## Newton's 3rd law
                Fy[j] = Fy[j] - fy
                Fz[j] = Fz[j] - fz
                ##virial = virial + (Fx[i]*Fx[i]+Fy[i]*Fy[i]+Fz[i]*Fz[i])*dsq    #???Virial F[j]

    ax, ay, az = 24*eps*Fx/m, 24*eps*Fy/m, 24*eps*Fz/m
    U = 4*eps*U
    return ax, ay, az, U, virial

#%%

def verlet(Vx, Vy, Vz,ax,ay,az, landa):
    Vx = Vx + 0.5*dt*ax
    Vy = Vy + 0.5*dt*ay
    Vz = Vz + 0.5*dt*az
    Vx = Vx *landa
    Vy = Vy *landa
    Vz = Vz *landa
    return Vx, Vy, Vz


#%%

def position_integration(rx, ry, rz, Vx, Vy, Vz,ax,ay,az):
    rx = rx + dt*Vx + 0.5*dt*dt*ax
    ry = ry + dt*Vy + 0.5*dt*dt*ay
    rz = rz + dt*Vz + 0.5*dt*dt*az
    return rx, ry, rz

#%%
#%%

def calc_Press():
    #### generate initial configuration
    KE = np.zeros(Nsteps)
    PE = np.zeros(Nsteps)
    TE = np.zeros(Nsteps)
    Tinst = np.zeros(Nsteps)
    Press = np.zeros(Nsteps)

    rx, ry, rz, Vx, Vy, Vz = initial_config()
    ax, ay, az, U, virial = force(rx, ry, rz, Vx, Vy, Vz)
    ke = np.sum(Vx*Vx+Vy*Vy+Vz*Vz)*0.5*m
    KE[0] = ke
    PE[0] = U
    TE[0] = ke + U
    Tinst[0] = (2 * KE[0]) / (3 * (N-1) * Kb)
    Press[0] = (N*Kb*Tinst[0]/vol) + ((1/3*vol)* virial)
    landa = 1

    for i in range(1, Nsteps):
        print (f"Progress:  {((i/Nsteps)*100):4.1f}%", end = '\r')
        rx, ry, rz = position_integration(rx, ry, rz, Vx, Vy, Vz,ax,ay,az)
        Vx, Vy, Vz = verlet(Vx, Vy, Vz,ax,ay,az, landa)
        ax, ay, az, U, virial = force(rx, ry, rz, Vx, Vy, Vz)
        Vx, Vy, Vz = verlet(Vx, Vy, Vz,ax,ay,az, landa)
        KE[i] = np.sum(Vx*Vx+Vy*Vy+Vz*Vz)*0.5*m
        PE[i] = U
        TE[i] = KE[i] + PE[i]
        Tinst[i] = (2 * KE[i]) / (3 * (N-1) * Kb)
        Press[i] = (N*Kb*Tinst[i]/vol) + ((1/(3*vol))* virial)
        landa = 1 + ((delt/tau)*((T/Tinst[i])-1))

    return (np.average(Press))

#%%

### MD runs ###
### read input file ###
Kb = 1.380649 * (10**(-23))
delt = 10**(-15)
tau = 10**(-12)
inputfil = 'params.a2.in'
params = read_data(inputfil)
##### Initialize parameters
sig, eps, m, ovrlap, rho_ar, dt, Nsteps, rcutsq, N, sig6, sig12, T, vol_ar, Lx_ar, Ly_ar, Lz_ar = initialize_parameters(params)

avg_press = np.zeros(len(rho_ar))

for i in range(len(rho_ar)):
    rho = float(rho_ar[i])
    vol = float(vol_ar[i])
    Lx = float(Lx_ar[i])
    Ly = float(Ly_ar[i])
    Lz = float(Lz_ar[i])
    avg_press[i] = calc_Press()
print ("avg_press=", avg_press)

#%%


