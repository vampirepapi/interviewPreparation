t=int(input())
for _ in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	# d=max(l)
	# c=min(l)
	# # print(d)
	# print(c)

	
	# e=l.index(d)
	# l.pop(e)
	# # print('index', e)
	# l.insert(e,c)
	# # print(l)
	# arr=[x//2 for x in l]
	# # for x in l:
	# # 	p=x//c
	# # 	arr.append(p)
	# print(sum(arr))

	def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
A = [8, 4, 2]
res = A[0]
for c in A[1::]:
    res = gcd(res , c)
print res

		
