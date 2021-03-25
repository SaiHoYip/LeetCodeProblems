#https://leetcode.com/problems/number-of-good-pairs/
class Solution(object):
    def __init__(nums):
        self.nums = nums
    def numIdenticalPairs(nums):
        count = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] == nums[j]) and i < j:
                    count = count + 1
        return count
    print(numIdenticalPairs([1,2,3,1,1,3]))
