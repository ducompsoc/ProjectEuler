import math

n = 600851475143
for i in range(3, math.floor(math.sqrt(n)), 2):
    while i < n and n % i == 0:
        n = n / i

print(int(n))
