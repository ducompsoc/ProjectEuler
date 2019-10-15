val = pow(2,1000)
vals = [int(val) for val in str(val)]
digSum = i = 0
while(i < len(vals)):
    digSum += vals[i]
    i+=1
print(digSum)
