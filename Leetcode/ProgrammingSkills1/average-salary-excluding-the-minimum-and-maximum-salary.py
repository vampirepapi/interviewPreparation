#ip/op to file
import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.in', 'w')

class Solution:
    def average(self, salary: List[int]) -> float:
        maxSalary = max(salary)
        minSalary = min(salary)
        avgSalary = (sum(salary)-(maxSalary+minSalary))/(len(salary)-2)
        return avgSalary
        