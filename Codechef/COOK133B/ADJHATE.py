# An array is called lovely if the sum of absolute differences of each adjacent pair of elements is odd; formally, the array S of size m is lovely if ∑m−1i=1 |Si−Si+1| is odd.

# You are given an array A of N integers. You need to reorder the array in any manner such that the array becomes lovely. If there is no reordering operation that makes the array lovely, output -1.

# Input Format
# The first line contains an integer T denoting the number of test cases. The T test cases then follow.
# The first line of each test case contains an integer N.
# The second line of each test case contains N space-separated integers A1,A2,…,AN.
# Output Format
# For each test case, print a single line containing N integers denoting the modified array which is lovely, or -1 if it is not possible.

# Constraints
# 1≤T≤1000
# 2≤N≤500
# 1≤Ai≤106
# Sample Input 1 
# 2
# 6
# 3 7 10 1 2 12
# 2
# 1 3
# Sample Output 1 
# 1 2 3 10 7 12
# -1
# Explanation
# For the first test case, the sum is |1−2|+|2−3|+|3−10|+|10−7|+|7−12|=1+1+7+3+5=17 which is odd.

# For the second test case, |1−3|=2 which is newArr. There is no array that can satisfy the above condition.

def solve():
  n=int(input())
  arr=list(map(int,input().split()))
  newArr=[]
  modArr=[]
  for i in arr:
    if i%2==0:
      newArr.append(i)
    else:
      modArr.append(i)
  if len(newArr) and len(modArr):
    print(*newArr,*modArr)
  else:
    print(-1)


if __name__ == '__main__':
  for i in range(int(input())):
    solve()