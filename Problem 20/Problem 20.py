num=100
fac=1
tot=0

# loop multiplying all numbers from 1 leading up to a specfied number 
for i in range (1,num+1):
    fac=fac*i

# the number has been assigned as both a string and an integer
# map() splits the number up into individual digits
# list() puts these digits separately into a list
num_list=list(map(int,str(fac)))


list_len=len(num_list)

# uses the number of values in the list as the max boundary for the loop counter
for j in range (0,list_len):
    tot=tot+num_list[j]

print(tot)
    






