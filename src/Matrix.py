class Matrix:
    def __init__(self, x, y):
         self.matrix = []
         self.x = x
         self.y = y
         for y in range(0, y):
             defaultArray = self.__createDefaultArray(x)
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

    def computeDerivative(self):
        if(self.x != self.y):
            return -1

    def insertValue(self,x, y, value):
        arr = self.matrix[x]
        arr[y] = value

    def getValue(self, x, y):
        return self.matrix[x][y]
