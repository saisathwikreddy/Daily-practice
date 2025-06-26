# Last updated: 6/26/2025, 2:34:57 PM
class Solution:
    def countNumConsec(self, s:str):
        l = []
        c = 1
        for i in range(1, len(s)):
            if s[i]==s[i-1]:c+=1
            else:
                l.append(f"{c}{s[i-1]}")
                c=1
        l.append(f"{c}{s[-1]}")
        return "".join(l)

    def countAndSay(self, n: int) -> str:
        s = '1' 
        for i in range(n-1):
            s = self.countNumConsec(s)
        return s

        