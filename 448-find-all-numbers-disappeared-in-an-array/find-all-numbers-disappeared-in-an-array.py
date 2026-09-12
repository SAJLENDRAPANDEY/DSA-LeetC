class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        seen=set(nums)
        n=len(nums)
        for i in range(1,len(nums)+1):
            if i not in seen:
                res.append(i)
        return res

        