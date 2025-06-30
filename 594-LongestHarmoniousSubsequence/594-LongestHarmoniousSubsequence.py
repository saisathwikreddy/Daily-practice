# Last updated: 6/29/2025, 10:20:47 PM
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dicti = {}
        for i in nums:
            if i not in dicti.keys():dicti[i] = 1
            else:dicti[i]+=1
        maxLen = 0
        for i in nums:
            if i+1 in dicti:
                maxLen = max(maxLen, dicti[i]+dicti[i+1])
        return maxLen