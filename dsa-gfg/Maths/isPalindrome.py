def palindromeNos(n):
	res = 0
	temp=n // creating temp var , call by value
	while temp>0:
		rem = temp%10
		temp=temp//10
		res = res*10 +rem
	#When you run a condition in an if statement, Python returns True or False.
	return res == n
	
print(palindromeNos(12))

#TC = theta(d) where d is no of digits in temp/n