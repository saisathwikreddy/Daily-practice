# Last updated: 7/5/2025, 9:07:00 PM
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq={}
        for i in nums2:
            if i not in self.freq:self.freq[i]=1
            else:self.freq[i]+=1

    def add(self, index: int, val: int) -> None:
        nums2, freq = self.nums2, self.freq
        freq[nums2[index]] -= 1
        nums2[index] += val
        if nums2[index] not in freq:freq[nums2[index]]=1
        else:freq[nums2[index]] += 1

    def count(self, tot: int) -> int:
        nums1, freq = self.nums1, self.freq
        c = 0
        for i in nums1:
            if tot-i in freq:c+=freq[tot-i]
        return c
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)