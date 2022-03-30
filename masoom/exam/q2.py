######### Q2
import numpy as np

np.set_printoptions(suppress=True, precision=3)

sourceList = [1, 2, 3, 4, 5, 6, 7, 8]
print(sourceList)

myData = np.array(sourceList)
print(myData)

myData = np.reshape(myData,(2,4))
print(myData)

arrayStdDev = np.std(myData,axis=1)
print(arrayStdDev)

transposeData = np.transpose(myData)
print(transposeData)

print(transposeData.ndim)
print(transposeData.shape)


