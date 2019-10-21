from math import floor, sqrt

# Implementation of Sieve of Eratosthenes to find primes <= maximum
# Sum them at the end
def prime_sieve(maximum):
    # Start by assuming every number is prime except 1
    primes = []
    sieved = [True] * maximum
    sieved[0] = False

    # Only need to search to the sqrt of the maximum as we will have
    # marked every composite number by this point
    root = floor(sqrt(maximum)) + 1

    # The number at index n is actually (n + 1)
    # Let a = n + 1
    for n in range(1, root):
        # If it is known to be composite just move on
        if sieved[n] == False:
            continue
    
        # Starting from 2 * a go to the maximum in increments of a
        # They must all be composite because they are multiples of a
        for x in range(2 * n + 1, maximum, n + 1):
            sieved[x] = False

    total_primes = 0

    # Take all the primes and sum them
    for i in range(0, maximum):
        if sieved[i] == True:
            total_primes += (i + 1)

    return total_primes

maximum = 2 * 10 ** 6
print(prime_sieve(maximum))
