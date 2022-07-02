
def largest(array):
    large = 0
    for i in range(len(array)):
        if large > array[i]:
            continue
        large = array[i]
    return large
meow = [2, 91, 4, 5, 6, 7, 8]
a = largest(meow)
meow.remove(a)
b = largest(meow)
print(a*b)

