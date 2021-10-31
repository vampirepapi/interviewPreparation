t=int(input())
for _ in range(t):
	a=input()
	l=len(a)
	split=l//2
	if len(a)%2==1:
		# print(a[:split+1],a[split:])
		if sorted(a[:split+1])==sorted(a[split:]):
			print("YES")
		else:
			print("NO")
	else:
		# print(a[:split],a[split:])
		if sorted(a[:split])==sorted(a[split:]):
			print("YES")
		else:
			print("NO")

