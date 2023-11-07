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

