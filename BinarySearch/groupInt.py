from collections import Counter
import math
L = [3, 4, 6, 9, 4, 3, 6, 9]
counts= Counter(L)
print(counts)
temp=0
for x in counts:
	#print(x)
	if temp==0:
		temp = counts[x]
		print("temp=",temp)

	else:
		temp=math.gcd(counts[x],temp)
		print("gcd_temp",temp)
		if temp == 1:
			print('False')
		#print("temp=",temp)
	
print('true')