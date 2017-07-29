class Matrix:
    def __init__(self, x, y):
         self.matrix = []
         self.x = x
         self.y = y
         defaultArray = self.__createDefaultArray(x)
         print(defaultArray)
         for y in range(0, y):
             self.matrix.append(defaultArray)

    def __createDefaultArray(self, length):
        arr = []
        for x in range(0, length):
            arr.append(0)
        return arr

    def printMatrix(self):
        for x in range(0, self.x):
            print(self.matrix[x])
        print()
