# Last updated: 6/26/2025, 2:34:49 PM
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        i,j = 0,len(nums)-1
        cU=0
        while i<j:
            if nums[i] + nums[j] <= upper:
                cU+=(j-i)
                i+=1
            else:
                j-=1
        i, j, cL = 0, len(nums)-1, 0
        while i<j:
            if nums[i] +nums[j] <lower:
                cL+=j-i
                i+=1
            else:
                j-=1
        return cU-cL


        