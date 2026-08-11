class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # i=0
        # for i in range(len(nums)):
        #     nums[i]=nums[i]*nums[i]
        # i+=1
        
        # nums.sort()
        # return nums
        























        i=0
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        i+=1
        nums.sort()
        return nums