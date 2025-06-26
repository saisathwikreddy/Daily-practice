# Last updated: 6/26/2025, 2:34:56 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = glo = nums[0]
        for i in range(1, len(nums)):
            curMax = max(nums[i],nums[i]+curMax)
            glo = max(curMax, glo)
        return glo