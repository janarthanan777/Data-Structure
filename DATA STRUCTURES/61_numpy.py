import numpy as np
twoArray = np.array([[1, 10, 33], [5, 9, 35], [24, 8, 37]])
newtwoArray = np.insert(twoArray, 3, [[1, 2, 3]], axis = 0)
print(newtwoArray)
