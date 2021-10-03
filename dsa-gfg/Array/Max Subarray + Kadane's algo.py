arr = [1, -2, 3, -1, 2]

res = arr[0]
for i in range(len(arr)):
	curr = 0
	for j in range(i,len(arr)):
		curr = curr + arr[j]
		res = max(res, curr)

print(res)

#TC = O(n**2)

#Efficient Approach:-
