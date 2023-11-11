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

