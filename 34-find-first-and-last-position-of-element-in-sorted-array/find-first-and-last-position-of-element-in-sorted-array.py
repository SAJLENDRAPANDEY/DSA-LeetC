class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first=-1
        last=-1
        res=set()
        for i in range(len(nums)):
            if nums[i]==target:
                first=i
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                last=j
                break
        return [first,last]