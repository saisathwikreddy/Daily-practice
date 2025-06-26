# Last updated: 6/26/2025, 2:34:54 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(1, numRows+1):
            a = 1
            k = [ a ]
            for j in range(1, i):
                a = a*(i-j)
                a = a//j
                k.append(a)
            l.append(k)
        return l