# Last updated: 7/25/2025, 7:52:13 PM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        l=[]
        if max(nums)<0:
            return max(nums)
        else:
            s=0
            for i in nums:
                if i>=0 and i not in l: 
                    l.append(i)
                    s+=i
            return s
                    

        