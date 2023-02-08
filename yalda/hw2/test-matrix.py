import numpy as np
print(np.zeros(3))

a=[1,2,3]
print(a)
m=[]
m.append(a)
m.append(np.zeros(3))
m[1][0]=1000
m[1][1]=2000
m[1][2]=3000
print(m)

n=np.transpose([a])
print(n)
# n.append(np.zeros(3))
# n = np.append(n, [np.zeros(3)], axis=1)
# print(np.zeros(3))
# n[:,-1] = np.zeros(3)
print(n)