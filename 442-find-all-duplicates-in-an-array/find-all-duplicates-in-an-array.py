class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        res=[]
        if len(nums)==1:
            return res
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in freq:
            if freq[num]>=2:
                res.append(num)
        return res