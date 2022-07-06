import time
list = [2, 5, 1, 3, 6, 9, 3, 4, 7, 2, 4,2, 1,46,7, 8,3, 9, 2, 6]
begtime = time.time()
for i in range(len(list)):
    min = i
    for j in range(i + 1, len(list)):
        if list[j] < list[min]:
            min = j
    list[i], list[min] = list[min], list[i]
endtime = time.time()
print(list)
print('Kitna time laga', endtime - begtime)