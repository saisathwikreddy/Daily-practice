# Last updated: 6/28/2025, 8:33:37 PM
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        vals = [[i, nums[i]] for i in range(len(nums))]
        vals.sort(key=lambda x:-x[1])
        vals = sorted(vals[:k])
        return [val for idx, val in vals]
        