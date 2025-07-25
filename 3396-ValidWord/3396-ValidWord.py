# Last updated: 7/25/2025, 7:52:12 PM
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:return False
        vowel = 'aeiouAEIOU'
        vowelCount, consonantCount, digitCount = 0, 0, 0
        for i in word:
            if i.isalpha():
                if i in vowel:vowelCount+=1
                else:consonantCount+=1
            elif i.isdigit():
                digitCount+=1
            else:
                return False
        if vowelCount<1 or consonantCount<1:return False
        return True
        