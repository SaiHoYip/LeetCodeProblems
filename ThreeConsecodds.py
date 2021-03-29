class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        odd = 0
        for a in range(len(arr)-2):
            if arr[a]%2 == 1 and arr[a+1]%2 == 1 and arr[a+2]%2 ==1:
                odd = 3
                return True
        return False

print(Solution.threeConsecutiveOdds('',[1,3,9,11,12]))
print(Solution.threeConsecutiveOdds('',[3,5,2,12]))