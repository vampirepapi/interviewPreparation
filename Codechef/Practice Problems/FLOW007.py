t=int(input())
for _ in range(t):
	n=input()
	print(n[::-1].lstrip('0'))

# Remove leading 0 from Strings List
# using lstrip() + list comprehension
# res = [ele.lstrip('0') for ele in test_list]
