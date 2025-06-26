# Last updated: 6/26/2025, 2:34:48 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fs = ''
        for i in range(min(len(word1), len(word2))):
            fs += word1[i] + word2[i]
        if len(word1)>min(len(word1),len(word2)):
            fs+=word1[min(len(word1),len(word2))::]
        else:
            fs+=word2[min(len(word1),len(word2))::]
        return fs