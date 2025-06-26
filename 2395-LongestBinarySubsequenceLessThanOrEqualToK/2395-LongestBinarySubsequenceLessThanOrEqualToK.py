# Last updated: 6/26/2025, 2:34:46 PM
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        crVal =0
        cnt =0
        bits = k.bit_length()
        for i,ch in enumerate(s[::-1]):
            if ch == '1':
                if i < bits and crVal + (1 << i) <= k:
                    crVal += 1 << i
                    cnt += 1
            else:
                cnt+=1
        return cnt
