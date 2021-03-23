#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/submissions/
class Solution:
    def __init__(self, num):
        self.num = num
    def numberOfSteps (num):
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num/2
                steps += 1
            else:
                num -= 1
                steps += 1
        return steps

print(Solution.numberOfSteps(14))



