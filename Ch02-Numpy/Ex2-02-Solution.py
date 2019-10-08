import numpy as np
array1 = np.arange(1, 10).reshape((3,3))
array2 = np.empty((3,3))
array2[:] = 2
print (array1 + array2)
print (array1 - array2)
print (array1 / array2)
print (array1 + 5)
print (array1[4:6])
array3 = np.arange(20)
aslice = array3[5:16]
print (aslice)
aslice[0] = 99
aslice[-1] = 99
print (aslice)

