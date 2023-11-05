# 1. Write Python code for a school management system with three user categories and show all three types of inheritance in it.
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_info(self):
        print(f"X: {self.x}, Y: {self.y}")

class B(A):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show_info(self):
        super().show_info()
        print(f"Z: {self.z}")

class C(A):
    def __init__(self, x, y, w):
        super().__init(x, y)
        self.w = w

    def show_info(self):
        super().show_info()
        print(f"W: {self.w}")

class D(C):
    def __init__(self, x, y, w, v):
        super().__init(x, y, w)
        self.v = v

    def show_info(self):
        super().show_info()
        print(f"V: {self.v}")

obj_b = B("John", 15, "S12345")
obj_c = C("Mr. Smith", 35, "T9876")
obj_d = D("Mrs. Johnson", 45, "P567", "A001")

print("Object B:")
obj_b.show_info()
print("\nObject C:")
obj_c.show_info()
print("\nObject D:")
obj_d.show_info()


# 2. Write a program that extends the class Employee. Derive a class Manager from Employee so that it lists all the details of the manager as well as the details of employees working under that manager.
class Karamchari:
    def __init__(self, emp_id, naam, vetan):
        self.emp_id = emp_id
        self.naam = naam
        self.vetan = vetan

    def dikhaao(self):
        print(f"Karamchari ID: {self.emp_id}")
        print(f"Naam: {self.naam}")
        print(f"Vetan: ₹{self.vetan}")


class Prabandhak:
    def __init__(self, prabandhak_id, naam, vetan):
        self.prabandhak_id = prabandhak_id
        self.naam = naam
        self.vetan = vetan
        self.anuyayi_karamchari = []

    def karamchari_jodo(self, karamchari):
        if isinstance(karamchari, Karamchari):
            self.anuyayi_karamchari.append(karamchari)
        else:
            print("Anvalid karamchari object.")

    def dikhaao(self):
        print(f"Prabandhak ID: {self.prabandhak_id}")
        print(f"Naam: {self.naam}")
        print(f"Vetan: ₹{self.vetan}")

        if self.anuyayi_karamchari:
            print("Anuyayi Karamchari:")
            for karamchari in self.anuyayi_karamchari:
                karamchari.dikhaao()
                print()


ram = Karamchari(101, "Ram", 50000)
shyam = Karamchari(102, "Shyam", 45000)
rajesh = Prabandhak(201, "Rajesh", 75000)
rajesh.karamchari_jodo(ram)
rajesh.karamchari_jodo(shyam)
print("Prabandhak Vivaran:")
rajesh.dikhaao()


#3. Write a program that extends the employee class so that it stores two more data members: DOB and Date_of_Hiring. The date must be defined as a separate class.
class A:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x:02d}/{self.y:02d}/{self.z}"

class B:
    def __init__(self, p, q, r, s):
        self.p = p
        self.q = q
        self.r = r
        self.s = s

    def __str__(self):
        return f"I: {self.p}\nN: {self.q}\nB: {self.r}\nH: {self.s}"

d = A(10, 5, 1990)
h = A(15, 8, 2020)

e = B("John Doe", 12345, d, h)

print(e)

#4. Write a program that extends the class Result so that, the final result of the student is evaluated based on the marks obtained in tests, activities, and sports.
class S:
    def __init__(self, n, r):
        self.n = n
        self.r = r
        self.t = 0
        self.a = 0
        self.s = 0
        self.f = None

    def st(self, m):
        self.t = m

    def sa(self, m):
        self.a = m

    def ss(self, m):
        self.s = m

    def c(self):
        t = self.t + self.a + self.s

        if t >= 90:
            self.f = "A+"
        elif t >= 80:
            self.f = "A"
        elif t >= 70:
            self.f = "B"
        elif t >= 60:
            self.f = "C"
        else:
            self.f = "F"

    def d(self):
        print(f"N: {self.n}")
        print(f"R: {self.r}")
        print(f"T: {self.t}")
        print(f"A: {self.a}")
        print(f"S: {self.s}")
        print(f"F: {self.f}")
        
    def gt_full_name(self):
        return f"{self.n} (Roll Number: {self.r})"

    def print_result_message(self):
        if self.f == "A+":
            print(f"Wow, {self.n} scored an A+! That's amazing!")
        elif self.f == "F":
            print(f"Oh no, {self.n} failed. Better luck next time!")
        else:
            print(f"{self.n}'s result is {self.f}.")
            
    def count_total_marks(self):
        return self.t + self.a + self.s

# Example usage:
class R:
    def __init__(self, n, r):
        self.n = n
        self.r = r
        self.t = 0
        self.a = 0
        self.s = 0
        self.f = None

    def st(self, m):
        self.t = m

    def sa(self, m):
        self.a = m

    def ss(self, m):
        self.s = m

    def c(self):
        t = self.t + self.a + self.s

        if t >= 90:
            self.f = "A+"
        elif t >= 80:
            self.f = "A"
        elif t >= 70:
            self.f = "B"
        elif t >= 60:
            self.f = "C"
        else:
            self.f = "F"

    def d(self):
        print(f"N: {self.n}")
        print(f"R: {self.r}")
        print(f"T: {self.t}")
        print(f"A: {self.a}")
        print(f"S: {self.s}")
        print(f"F: {self.f}")


# Example usage:
student = R("Ishmeet", "12345")
student.st(75)
student.sa(85)
student.ss(90)
student.c()
student.d()

