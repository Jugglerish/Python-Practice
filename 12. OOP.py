
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
