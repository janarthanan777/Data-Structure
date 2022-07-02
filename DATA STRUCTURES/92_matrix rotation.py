import numpy as np
def rotate(matrix):
    tempe = 0
    print(matrix)
    n = len(matrix)
    for x in range(n//2):
        for i in range(x, n - x - 1):
            tempe = matrix[x][i]
            matrix[x][i] = matrix[n - i - 1][x]
            matrix[n - i - 1][x] = matrix[n - x - 1][n - 1 - i]
            matrix[n - x - 1][n - 1 - i] = matrix[i][n - x - 1]
            matrix[i][n - x - 1] = tempe
    print(matrix)
myArray = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]])
rotate(myArray)