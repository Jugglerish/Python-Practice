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

