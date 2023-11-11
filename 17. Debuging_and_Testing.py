
# . Write a function for finding a prime number. Introduce a known bug. Use Pdb to debug it.
def pn(n):
    ps = []
    for i in range(2, n+1):
        isp = True
        for j in range(2, i):
            if i % j == 0:
                isp = False
                break
        if isp:
            ps.append(i)
    return ps

import pdb

n = 10
pdb.set_trace()
pns = pn(n)
print(f"pRiMe numbeRS up to {n}: {pns}")



# 2. Write a function for finding a perfect number and use Pdb to debug it.
import pdb

def pfct_nmbr(num):
    pdb.set_trace()
    sum_divs = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divs += i
    return sum_divs == num

if __name__ == "__main__":
    input_num = int(input("Enter a number: "))
    result = pfct_nmbr(input_num)
    if result:
        print(f"The number {input_num} is a perfect number.")
    else:
        print(f"The number {input_num} is not a perfect number.")



# 3. Write a program for finding linear and binary searches. Determine the profiling of both functions and justify the better search method based on profiling results.
import time
def ls(a, x): return any(i == x for i in a)
def bs(a, x): l, h = 0, len(a) - 1; while l <= h: m = (l + h) // 2; if a[m] == x: return True; elif a[m] < x: l = m + 1; else: h = m - 1; return False
sz, v = 10000, 9999
arr = list(range(sz))
lt = time.time(); ls(arr, v); lst = time.time() - lt
bt = time.time(); bs(arr, v); bst = time.time() - bt
print(f"L Search Time: {lst} sec"); print(f"B Search Time: {bst} sec")
print("Linear is better." if lst < bst else "Binary is better.")



# 4. Apply a profiler for a Python program that finds a perfect number.
import cProfile

def perf_num(limit):
    perf_nums = [num for num in range(1, limit + 1) if sum(d for d in range(1, num) if num % d == 0) == num]
    return perf_nums

if __name__ == "__main__":
    lim = 10000

    profiler = cProfile.Profile()
    profiler.enable()

    result = perf_num(lim)

    profiler.disable()
    profiler.print_stats(sort='cumulative')
    print(f"Perfect numbers up to {lim}: {result}")


# 5. Write a function for multiplication and division. Apply to a doctest to verify it.
def mul_div(a, b):
    mul = a * b
    div = a / b if b != 0 else float('inf')
    return mul, div

if __name__ == "__main__":
    import doctest
    doctest.testmod()


#6. Use unittest for testing a multiplication program
import unittest

def mul(a, b):
    return a * b

class T(unittest.TestCase):
    def t_p(self):
        self.assertEqual(mul(2, 3), 6)

    def t_n(self):
        self.assertEqual(mul(-4, 2), -8)

    def t_z(self):
        self.assertEqual(mul(0, 5), 0)

    def t_zz(self):
        self.assertEqual(mul(0, 0), 0)

if __name__ == '__main__':
    unittest.main()



# 7. Write test cases for finding a prime number
import unittest

def p(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

class T(unittest.TestCase):
    def tn(self):
        self.assertFalse(p(-5))

    def tz(self):
        self.assertFalse(p(0))

    def to(self):
        self.assertFalse(p(1))

    def tsp(self):
        self.assertTrue(p(2))

    def tpp(self):
        self.assertTrue(p(17))

    def tpnp(self):
        self.assertFalse(p(15))

    def tlp(self):
        self.assertTrue(p(97))

if __name__ == '__main__':
    unittest.main()

# 8. Write test cases for finding the perfect number
def xyz(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n

def test_xyz():
    assert xyz(6) == True
    assert xyz(28) == True
    assert xyz(12) == False
    assert xyz(496) == True
    assert xyz(10) == False
    assert xyz(8128) == True
    assert xyz(15) == False
    assert xyz(33550336) == True
    assert xyz(20) == False
    assert xyz(28) == True

test_xyz()


# 9. Use unittest for checking whether a number is a perfect number or not
import unittest

def is_perfect_number(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n

class TestPerfectNumber(unittest.TestCase):

    def test_perfect_number(self):
        self.assertTrue(is_perfect_number(6))
        self.assertTrue(is_perfect_number(28))
        self.assertFalse(is_perfect_number(12))
        self.assertTrue(is_perfect_number(496))
        self.assertFalse(is_perfect_number(10))
        self.assertTrue(is_perfect_number(8128))
        self.assertFalse(is_perfect_number(15))
        self.assertTrue(is_perfect_number(33550336))
        self.assertFalse(is_perfect_number(20))
        self.assertTrue(is_perfect_number(28))

if __name__ == '__main__':
    unittest.main()



# 10. Use the pytest to verify whether a number is a prime number or not.
import pytest

p=lambda n:all(n%i!=0 for i in range(2,n))if n>1else False

def t1():assert p(2)
def t2():assert not p(4)
def t3():assert p(7)
def t4():assert not p(9)

if __name__=="__main__":pytest.main()


