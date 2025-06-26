# Last updated: 6/26/2025, 2:34:53 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0] 
        prof = 0
        for i in prices[1:]:
            mini = min(i, mini)
            prof = max(prof, i-mini)
        return prof