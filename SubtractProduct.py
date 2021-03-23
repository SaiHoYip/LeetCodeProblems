#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        product = 1
        for t in str(n):
            summ += int(t)
            product *= int(t)
        difference = product - summ
        return product - summ

print(Solution.subtractProductAndSum(1,234))
