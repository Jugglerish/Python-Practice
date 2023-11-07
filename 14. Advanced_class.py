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
