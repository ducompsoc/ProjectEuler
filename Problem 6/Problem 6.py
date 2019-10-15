sum_sqr=0
sqr_sum=0
sum_num=0
dif=0

# loop to automatically increase i by 1 to 101
for i in range (1,101):
	#101 is used because the max boundary is always one less than the number stated (n-1)
	
	sum_sqr=(i**2)+sum_sqr	#running total for the sum of squared numbers up to 100
	sum_num=i+sum_num	#running total for the sum of numbers up to 100

sqr_num=(sum_num)**2 #squares the sum 

print(sqr_num-sum_sqr)




