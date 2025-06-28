# Last updated: 6/27/2025, 8:10:19 PM
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isK(sub:str, t:str, k:int)->bool:
            co = i = 0
            for ch in t:
                if i < len(sub) and ch == sub[i]:
                    i+=1
                    if i==len(sub):
                        i=0
                        co+=1
                        if co == k:
                            return True
            return False
        r = ""
        q = deque([""])
        while q:
            c = q.popleft()
            for ch in map(chr, range(ord('a'),ord('z') + 1)):
                nxt = c + ch
                if isK(nxt, s, k):
                    r = nxt
                    q.append(nxt)
        return r
        