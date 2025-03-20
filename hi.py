n = int(input("Enter Number: "))
if (n<2):
	print(f"{n} is neither prime nor composite")
elif (n>=2):
	for i in range(2,n):
		if(n%i == 0):
			print(f"{n} is not prime")
			break
	else:
		print(f"{n} is Prime Number")
