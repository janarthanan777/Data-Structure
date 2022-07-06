from array import *
arrayName = array('i', [1, 2, 3, 4])
arrayName.insert(0, 9)
for i in range(len(arrayName)):
    print(arrayName[i])
print(arrayName.buffer_info())



