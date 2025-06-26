# Last updated: 6/26/2025, 2:34:57 PM
class Solution:
    def swap(self, nums,  i, j):
        t = nums[i]
        i = nums[j]
        nums[j] = t
    def reverse(self, nums, start):
        i, j = start, len(nums)-1
        while i<j:
            self.swap(nums, i, j)
            i+=1
            j-=1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakIndex = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<nums[i+1]:
                breakIndex = i
                break
        if breakIndex == -1: 
            nums.reverse()
        else:
            for i in range(len(nums)-1, breakIndex, -1):
                if nums[breakIndex] < nums[i]:
                    nums[breakIndex], nums[i] = nums[i], nums[breakIndex]
                    break
            nums[breakIndex+1:] = reversed(nums[breakIndex+1::])
