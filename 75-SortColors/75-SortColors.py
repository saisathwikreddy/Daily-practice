# Last updated: 6/26/2025, 2:34:54 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,m,h =0,0,len(nums)-1
        while m<=h:
            if nums[m]==0:
                nums[l],nums[m] = nums[m],nums[l]
                l+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[h],nums[m] = nums[m], nums[h]
                h-=1
        
        
        