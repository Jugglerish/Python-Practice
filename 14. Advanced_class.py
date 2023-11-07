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

# 4. Write a Python program to overload the relation operator, less than or equal to the compare two lists, namely, list1 and list2, and print the number of elements in list1 that are lesser than or equal to the elements in list2.
class ListComparer:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __le__(self, other):
        if len(self.list1) != len(self.list2):
            raise ValueError("Both lists must have the same length for comparison.")
        count = 0
        for elem1, elem2 in zip(self.list1, self.list2):
            if elem1 <= elem2:
                count += 1
        return count

list1 = [1, 2, 3, 4, 5]
list2 = [3, 3, 3, 3, 3]

comparison = ListComparer(list1, list2)
count = comparison <= list2
print(f"Number of elements in list1 that are <= list2: {count}")

# 5. Write a Python program to print the school name, class, and section using the method overriding with the help of multilevel inheritance.
class A:
    def __init__(self, a):
        self.a = a

    def show(self):
        print(f"School: {self.a}")


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def show(self):
        super().show()
        print(f"Class: {self.b}")


class C(B):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def show(self):
        super().show()
        print(f"Section: {self.c}")


school = "Example School"
class_name = "Class 10"
section = "A"

obj = C(school, class_name, section)
obj.show()

# . Write a Python program to evaluate whether the student is overall passing or not where it has a hierarchy of classes to store the students and the marks. The passing criteria for a subject a the student should have obtained 50 marks. If the student is passed in all subjects, then he is overall passed or else not.
class S:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def p(self):
        return self.s >= 50

class St:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def o(self):
        for i in self.s:
            if not i.p():
                return False
        return True

if __name__ == "__main__":
    s = [
        S("Math", 65),
        S("Science", 55),
        S("English", 40),
    ]

    st = St("John Doe", s)

    if st.o():
        print(f"{st.n} is overall passing.")
    else:
        print(f"{st.n} is not overall passing.")

#7. Write a Python program for user management for a school management system using abstract base class (ABC).
from abc import ABC, abstractmethod

class A(ABC):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @abstractmethod
    def d(self):
        pass

class B(A):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def e(self):
        print(f"A: a: {self.a}, b: {self.b}, c: {self.c}")

class C(A):
    def __init__(self, a, b, c, e):
        super().__init__(a, b, c)
        self.e = e

    def f(self):
        print(f"B: a: {self.a}, b: {self.b}, c: {self.c}")

def g():
    b_objects = []
    c_objects = []

    while True:
        print("1. Create B")
        print("2. Create C")
        print("3. Display Bs")
        print("4. Display Cs")
        print("5. Exit")

        h = input("Enter your choice: ")

        if h == '1':
            a = input("Enter a: ")
            b = input("Enter b: ")
            c = input("Enter c: ")
            d = input("Enter d: ")
            b_object = B(a, b, c, d)
            b_objects.append(b_object)

        elif h == '2':
            a = input("Enter a: ")
            b = input("Enter b: ")
            c = input("Enter c: ")
            e = input("Enter e: ")
            c_object = C(a, b, c, e)
            c_objects.append(c_object)

        elif h == '3':
            print("Bs:")
            for b_object in b_objects:
                b_object.e()

        elif h == '4':
            print("Cs:")
            for c_object in c_objects:
                c_object.f()

        elif h == '5':
            break

if __name__ == "__main__":
    g()

