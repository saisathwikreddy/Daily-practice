# Last updated: 6/27/2025, 8:10:18 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)-{0})