from random import random

L=8
Rx=[None]*L
Rx[1]=random() * L
Rx[0]=random() * L
print('Rx=',Rx)
RXD = Rx[1] - Rx[0]
print('RXD=',RXD)
RXD = RXD - round(RXD/L)*L
print('RXD=',RXD,RXD/L,round(RXD/L),round(RXD/L)*L)
