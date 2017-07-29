from __init__ import *

matrix = Matrix(3,3)
matrix.insertValue(0, 0, 20)
matrix.insertValue(1, 0, 5)
matrix.insertValue(0, 1, 6)
matrix.insertValue(1, 1, 14)
matrix.printMatrix()
print(matrix.trimMatrix(0))
