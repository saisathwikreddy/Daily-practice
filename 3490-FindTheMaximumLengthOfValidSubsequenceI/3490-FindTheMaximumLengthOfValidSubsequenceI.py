# Last updated: 7/25/2025, 7:52:14 PM
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_dp, odd_dp, odd, even = 0, 0, 0, 0
        for i in nums:
            if i%2: 
                odd_dp = max(odd_dp, even_dp+1)
                odd +=1
            else: 
                even_dp = max(even_dp, odd_dp+1)
                even+=1
        return max(odd, even, even_dp, odd_dp)
