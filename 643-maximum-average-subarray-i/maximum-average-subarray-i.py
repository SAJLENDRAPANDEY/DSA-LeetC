class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_a=sum(nums[:k])
        max_a=window_a
        for i in range(k,len(nums)):
            window_a+=nums[i]
            window_a-=nums[i-k]

            max_a=max(max_a,window_a)
        return float(max_a)/k