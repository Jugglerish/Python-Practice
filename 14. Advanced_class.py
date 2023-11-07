#1. Write a program to find the increment of all the elements in a list with value 2 by overloading the unary "+" operator in Python
class IncLst:
    def __init__(self, d):
        self.d = d

    def __pos__(self):
        l = [x + 2 for x in self.d]
        return IncLst(l)

    def __str__(self):
        return str(self.d)

ol = [1, 3, 5, 7]
inc = +IncLst(ol)
print("Original List:", ol)
print("Incremented List:", inc)

# 2. Using the concept of operator overloading, implement the operator "*" to perform matrix multiplication for any 3X3 matrices in Python where matrices should be stored in list format.
class M:
    def __init__(s, e):
        if len(e) != 3 or any(len(r) != 3 for r in e):
            raise ValueError("Invalid matrix size")
        s.e = e

    def __str__(s):
        return "\n".join([" ".join(map(str, r)) for r in s.e])

    def __mul__(s, o):
        if not isinstance(o, M):
            raise ValueError("Invalid multiplication")

        r = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    r[i][j] += s.e[i][k] * o.e[k][j]

        return M(r)

m1 = M([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = M([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

r = m1 * m2
print("Matrix 1:")
print(m1)
print("\nMatrix 2:")
print(m2)
print("\nMatrix 1 * Matrix 2:")
print(r)

# 3. Using abstract class, implement matrix determinant with two abstract methods, three CrossThreeDeterminants and two CrossTwo Determinants.
from abc import ABC, abstractmethod

class MatrixDeterminantCalculator(ABC):
    @abstractmethod
    def determinant_3x3(self, matrix):
        pass

    @abstractmethod
    def determinant_2x2(self, matrix):
        pass

class DeterminantCalculator(MatrixDeterminantCalculator):
    def determinant_3x3(self, matrix):
        if len(matrix) != 3 or len(matrix[0]) != 3:
            raise ValueError("Matrix must be 3x3 for determinant_3x3 calculation.")
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]
        return a * e * i + b * f * g + c * d * h - c * e * g - a * f * h - b * d * i

    def determinant_2x2(self, matrix):
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise ValueError("Matrix must be 2x2 for determinant_2x2 calculation.")
        a, b = matrix[0]
        c, d = matrix[1]
        return a * d - b * c

calculator = DeterminantCalculator()

matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2x2 = [[2, 3], [4, 5]]

determinant_3x3 = calculator.determinant_3x3(matrix_3x3)
determinant_2x2 = calculator.determinant_2x2(matrix_2x2)

print(f"Determinant of 3x3 matrix: {determinant_3x3}")
print(f"Determinant of 2x2 matrix: {determinant_2x2}")
