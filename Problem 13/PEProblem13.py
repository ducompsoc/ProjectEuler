import io
file = open("numbers.txt")
sumOfValues = 0
for line in file:
    sumOfValues += int(file.readline())

print(str(sumOfValues)[:10])
    
