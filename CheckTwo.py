#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        string1 = ""
        string2 = ""
        for a in word1:
            string1 += a
        for t in word2:
            string2 += t
        if string1 == string2:
            return True
        else:
            return False

print(Solution.arrayStringsAreEqual('',['ab','c'],['a','bc']))