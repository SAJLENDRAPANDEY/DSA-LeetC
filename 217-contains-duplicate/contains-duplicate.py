class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in freq:
            if freq[num]>1:
                return True
        return False
        