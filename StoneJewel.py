class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        StoneJewels = 0
        for i in range(len(jewels)):
            for e in range(len(stones)):
                if jewels[i] == stones[e]:
                    StoneJewels += 1
        return StoneJewels

print(Solution.numJewelsInStones(0,'aaaAAbbbb', 'aA'))