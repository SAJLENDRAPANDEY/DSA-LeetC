class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # lef=0
        # for right in range(lef+1,len(nums)):
        #     if nums[lef]+nums[right]==target:
        #         return (lef,right)
        #     lef+=1

        # for i in range(len(nums)):
        #     for j in range(len(nums)-1,-1):
        #         if nums[i]+nums[j]==target:
        #             return ([i,j])
        # nums.sort()
        # left=0
        # right=len(nums)-1
        # while left<right:
        #     s=nums[left]+nums[right]
        #     if s==target:
        #         return(left,right)
        #     elif s<target:
        #         left+=1
        #     else:
        #         right-=1

        # for i  in range(len(nums)):)
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return (i,j)
        

        # freq={}
        # for index,num in enumerate(nums):
        #     req=target-num
        #     if req in freq:
        #         return (freq[req],index)
        #     freq[num]=index





























        seen={}
        for i , num in enumerate(nums):
            freq=target-num
            if freq in seen:
                return (seen[freq],i)
            seen[num]=i