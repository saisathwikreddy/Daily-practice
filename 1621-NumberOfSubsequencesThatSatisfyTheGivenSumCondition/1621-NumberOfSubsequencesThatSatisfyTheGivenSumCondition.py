# Last updated: 6/29/2025, 12:55:21 PM
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9+7
        power = [1]*len(nums)
        for i in range(1,len(nums)):power[i] = (power[i-1]*2)%mod
        l, r = 0, len(nums)-1
        res = 0
        while l<=r:
            if nums[l]+nums[r]<=target:
                res = (res + power[r-l])%mod
                l+=1
            else:
                r-=1
        return res
