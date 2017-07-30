import random

class Matrix:
    def __init__(self, x, y):
         self.matrix = []
         self.x = x
         self.y = y
         for x in range(0, self.x):
             defaultArray = self.__createDefaultArray(self.y)
             self.matrix.append(defaultArray)

    def __createDefaultArray(self, length):
        arr = []
        for x in range(0, length):
            arr.append(0)
        return arr

    def printMatrix(self):
        line = ""
        for x in range(0, self.x):
            for y in range(0, self.y):
                line += " " + str(self.matrix[x][y])
            print(line)
            line = ""

    def createMatrixWithArray(self, matrix) :
        matr = Matrix(2, 2)
        matr.matrix = matrix
        matr.x = len(matrix)
        matr.y = len(matrix[0])
        return matr

    def computeDeterminant(self):
        if(self.x != self.y):
            return -1
        if(self.x == 2):
            return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[1][0] * self.matrix[0][1])
        determinant = 0
        for y in range(0, self.y):
            mult = self.matrix[0][y]
            subMatrix = self.createMatrixWithArray(self.__trimMatrix(y))
            if(y % 2 == 0):
                determinant += mult * subMatrix.computeDeterminant()
            else:
                determinant -= mult * subMatrix.computeDeterminant()
        return determinant

    def insertValue(self,x, y, value):
        arr = self.matrix[x]
        arr[y] = value

    def getValue(self, x, y):
        return self.matrix[x][y]

    def getRow(self, x):
        return self.matrix[x]

    def __trimMatrix(self, yExclude):
        arr = []
        for x in range(1, self.x):
            row = []
            for y in range(0, self.y):
                if(y != yExclude):
                    row.append(self.matrix[x][y])
            arr.append(row)
        return arr

def fillSquareMatrixWithRandomData(matrix):
    size = matrix.x
    for x in range(0, size):
        for y in range(0, size):
            ran = random.randint(1, 6)
            matrix.insertValue(x, y, ran)
