list = [2, 5, 1, 3, 6, 9, 3, 4]
for i in range(len(list)):
    min = 0
    max = 1
    x = 0
    swap = False
    for j in range(len(list)- 1):
        if list[min] > list[max]:
            list[min], list[max] = list[max], list[min]
            min += 1
            max += 1
            swap = True
        else:
            min += 1
            max += 1
    if swap == False:
        break
print(list)