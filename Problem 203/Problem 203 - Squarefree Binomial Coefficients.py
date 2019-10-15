from math import sqrt, floor

# Generates n rows of Pascal's Triangle
def pascals_triangle(n):
    topDown = [[1]]

    # Loops to generate the remaining (n - 1) rows 
    for row_index in range(0, n - 1):
        above = topDown[row_index]
        row = [1]

        # Sum the two elements above to get the next coefficient
        for i in range(1, row_index + 1):
            row.append(above[i - 1] + above[i])

        # All rows n (n > 1) are of the form 1 ... 1
        row.append(1)
        topDown.append(row)

    return topDown

# Flattens a 2D array into a single array
def flatten_array(nested_array):
    flat = []
    
    for array in nested_array:
        for element in array:
            flat.append(element)

    return flat

    #return set([element for array in nested_array for element in array])

# Implementation of Sieve of Eratosthenes to find primes <= maximum
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

    # Take all the primes and put them in a list
    for i in range(0, maximum):
        if sieved[i] == True:
            primes.append(i + 1)

    return primes

# Take ~5ms for rows = 51
def distinct_squarefree(rows):
    # Get the triangle and flatten it
    # Then use a set to remove duplicates as each element has to be unique
    triangle = pascals_triangle(rows)
    flattened = flatten_array(triangle)
    distinct = set(flattened)

    # Since we are looking at squared primes dividing the numbers then:
    # a = 0 (mod p^2) then sqrt(a) = 0 (mod p) so only need to seach up to
    # sqrt(sqrt(a))
    max_number = max(distinct)
    max_root = floor(sqrt(sqrt(max_number))) + 1

    # Interested in the square of the primes so find the primes and square each
    squared_primes = [x ** 2 for x in prime_sieve(max_root)]

    # Try each square if it divides the coefficient it isn't square-free
    # Can't remove elements from a set in a loop so mark them in a seperate set
    # Then remove them after the loop is finished
    for square in squared_primes:
        marked = set()
        
        for n in distinct:
            if square > n:
                continue
            
            if n % square == 0:
                marked.add(n)

        for n in marked:
            distinct.remove(n)
            
    # Sum the remaining and that is the solution
    return sum(distinct)

print(distinct_squarefree(8))

