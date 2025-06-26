# Last updated: 6/26/2025, 2:34:47 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n1, n2 = 0, 0
        for i in range(1, n+1):
            if i%m == 0:n1+=i
            else:n2+=i
        return n2-n1
        