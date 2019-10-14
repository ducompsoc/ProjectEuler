tot, a, b = 0, 0, 1 #define variables
while(a < 4000000):
    if(a%2==0): #if a value in the fibonacci sequnce is positive...
        tot += a #...add it to the running total
    a, b = b, a + b #b becomes the next term in the fibonnaci sequence, while a adopts b's previous value
print(tot)
