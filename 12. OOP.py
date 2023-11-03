
# using OOP. The details to receive are staff_id, basic_pay, years_of_experience, total_allowance and total_deduction with the help of Constructor. Using methods calculate net_pay
class staff:
def __init__(s, id, basicpay, experience, allowance, deduction):
    s.id = id
    s.basicpay = basicpay
    s.experience = experience
    s.allowance = allowance
    s.deduction = deduction
def calculate_netpay(s):
gross = s.basicpay + s.allowance
net = gross - s.deduction
return net

e = staff("S123", 50000, 5, 2000, 1000)
n = e.calculate_netpay()
print(f"Employee ID: {e.id}")
print(f"Net Salary: ${n}")


# 3. Write a program to calculate area, perimeter and height of the triangle using the concept of classes and objects.
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

base = 5.0
height = 3.0

triangle = Triangle(base, height)

area = triangle.calculate_area()
print(area)



#4. Write a static method that check whether all words in the list starts with vowel.
class VowelsCheck:
    @staticmethod
    def lets_check_vowels(word_lst):
        vowels = 'AEIOUaeiou'

        for word in word_lst:
            if word[0] not in vowels:
                return False
        return True

words = ["apple", "orange", "elephant", "banana"]
result = VowelsCheck.lets_check_vowels(words)

if result:
    print("All words start with a vowel.")
else:
    print("Not all words start with a vowel.")



# 5. Write a program which receives either basic_pay and total_allowance or net pay and print the net_pay using separate method and calculation of net pay from basic_pay and allowance should be done using classmethod.
class C:
    def __init__(s, b=0, a=0):
        s.b = b
        s.a = a

    @classmethod
    def c(cls, b, a):
        return b + a

    def m(s):
        return s.c(s.b, s.a)

    def d(s, n):
        print(f"N: ${n}")

if __name__ == "__main__":
    c = input("1 for calc or 2 for net: ")

    if c == '1':
        b = float(input("B: $"))
        a = float(input("A: $"))
        x = C(b, a)
        n = x.m()
        x.d(n)
    elif c == '2':
        n = float(input("N: $"))
        x = C()
        x.d(n)
    else:
        print("Bad input. Enter '1' or '2'.")


# 6. Add a method reflect to class Point, which returns a new about the x axis and y axis. For example, Point(1,2), point which is the reflection of the point reflection is Point (-1,-2).
class P:
    def __init__(s, x, y):
        s.x, s.y = x, y
    def __str__(s):
        return f"{s.x},{s.y}"
    def r(s):
        return P(s.x, -s.y)

print(P(3, 5).r())


# 7. Create a Class for Bank which holds few details about the bank and define destructor which should make all the variables as "None" and print the message "The Process ends".
class Bnk:
    def __init__(self, nm, loc, acnt_cnt):
        self.nm = nm
        self.loc = loc
        self.acnt_cnt = acnt_cnt

    def __del__(self):
        self.nm = None
        self.loc = None
        self.acnt_cnt = None
        print("The Process ends")
b = Bnk("MyBank", "New York", 1000)
del b


# Create an OOP Program to determine the value and characteristics of the roots. Roots includes both real and complex numbers.
import math

class RootsCalculator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_roots(self):
        discriminant = self.b**2 - 4 * self.a * self.c

        if discriminant > 0:
            return "Two real roots"
        elif discriminant == 0:
            return "One real root"
        else:
            return "Complex roots"

if __name__ == "__main__":
    a = float(input("Enter the coefficient of x^2 (a): "))
    b = float(input("Enter the coefficient of x (b): "))
    c = float(input("Enter the constant term (c): "))
    
    calculator = RootsCalculator(a, b, c)
    result = calculator.calculate_roots()
    print(f"Roots: {result}")


# 9. Write an OOP program which reads 2 points and performs following functions with users choice
           # i. Distance between 2 points.
            #ii. Slope between 2 points.
           # iii. Checking whether the two points are inside/ outside/on the circle x²+ y²= 16
import math

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class B:
    def __init__(self, r):
        self.r = r

    def c(self, p):
        return p.a**2 + p.b**2 < self.r**2

    def o(self, p):
        return p.a**2 + p.b**2 == self.r**2

    def i(self, p):
        return p.a**2 + p.b**2 > self.r**2

def u():
    print("Choose an operation:")
    print("1. Calculate distance between two points")
    print("2. Calculate slope between two points")
    print("3. Check if two points are inside/outside/on the circle")
    return int(input("Enter your choice (1/2/3): ")

def m():
    a1, b1 = map(float, input("Enter coordinates of the first point (a1 b1): ").split())
    a2, b2 = map(float, input("Enter coordinates of the second point (a2 b2): ").split())
    
    p1 = A(a1, b1)
    p2 = A(a2, b2)
    
    c = u()
    
    if c == 1:
        d = math.sqrt((p2.a - p1.a)**2 + (p2.b - p1.b)**2)
        print(f"Distance between the two points: {d:.2f}")
    elif c == 2:
        if p2.a - p1.a == 0:
            print("Slope is undefined (vertical line).")
        else:
            s = (p2.b - p1.b) / (p2.a - p1.a)
            print(f"Slope between the two points: {s:.2f}")
    elif c == 3:
        r = 4  # Radius of the circle a^2 + b^2 = 16
        C = B(r)
        if C.o(p1) and C.o(p2):
            print("Both points are on the circle.")
        elif C.i(p1) and C.i(p2):
            print("Both points are inside the circle.")
        elif C.c(p1) and C.c(p2):
            print("Both points are outside the circle.")
        else:
            print("One point is inside and one is outside the circle.")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

m()


# 10. Write a menu driven program to calculate perimeter and number of diagonals with number of sides as input.
def p(n, s):
    perim = n * s
    return perim

def d(n):
    diag = (n * (n - 3)) / 2
    return diag

while True:
    print("Menu:")
    print("1. Calculate Perimeter")
    print("2. Calculate Number of Diagonals")
    print("3. Exit")
    
    c = input("Enter your choice (1/2/3): ")

    if c == '1':
        n = int(input("Enter the number of sides: "))
        s = float(input("Enter the side length: "))
        perim = p(n, s)
        print(f"Perimeter: {perim}")
    elif c == '2':
        n = int(input("Enter the number of sides: "))
        diag = d(n)
        print(f"Diagonals: {diag}")
    elif c == '3':
        print("Exit. Bye!")
        break
    else:
        print("Invalid choice. Select 1, 2, or 3.")


