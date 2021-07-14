nums = [8,1,2,2,3]
count=0
# for x in range (len(nums)):
#     for j in range(x+1,len(nums)):
#         if nums[x] > nums[j]:
#             count+=1
#         else:
#             count += 0
# print(count)
ans = []
print(nums)
sort = sorted(nums)
print(sort)
for i in nums:
    l=(sort.index(i))
    print(l)
    ans.append(l)
print(ans)