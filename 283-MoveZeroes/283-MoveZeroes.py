# Last updated: 6/26/2025, 2:34:51 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i],nums[k]
                k+=1
