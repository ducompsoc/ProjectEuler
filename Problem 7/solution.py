import math
A = [True]*500000
A[1] = False

# sieve
for i in range(2, int(math.sqrt(500000)+1)):
    if A[i]:
        for j in range(i**2, 500000, i):
            A[j] = False

primes = []
for x in range(len(A)):
    if A[x]:
        primes.append(x)

print(primes[10001])

