import sys
from random import random
import json
from configparser import ConfigParser

config = ConfigParser()
config.read('assignment2.data')

print( config )

L = config.getint('default','L') # 8
dcutsq = config.getfloat('default','dcutsq') # 0.64
rho = config.getfloat('default','rho') # 0.5
N = int(L*L*L*rho)

dsq_min=sys.maxsize

Rx,Ry,Rz=[None]*N,[None]*N,[None]*N
Rx[0] = random() * L
Ry[0] = random() * L
Rz[0] = random() * L
for i in range(1,N):
    Flag = 1
    while Flag == 1:
        Rx[i] = random() * L
        Ry[i] = random() * L
        Rz[i] = random() * L
        for j in range(0,i):
            RXD = Rx[i] - Rx[j]
            RXD = RXD - round(RXD/L)*L
            RYD = Ry[i] - Ry[j]
            RYD = RYD - round(RYD/L)*L
            RZD = Rz[i] - Rz[j]
            RZD = RZD - round(RZD/L)*L

            Dsq = RXD*RXD + RYD*RYD + RZD*RZD
            print("i=%s,j=%s,Dsq=%s"%(i,j,Dsq))
            if Dsq < dcutsq:
                Flag = 0
                if dsq_min>Dsq:
                    dsq_min=Dsq

print('Dsq_min=',dsq_min)