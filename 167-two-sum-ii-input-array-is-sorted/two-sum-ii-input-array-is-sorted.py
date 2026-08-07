class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # left=0
        # right=len(numbers)-1
        # # for i in range(len(numbers)):
        # #     for j in range(i+1,len(numbers)):
        # #         if numbers[i]+numbers[j]==target:
        # #             return i+1,j+1
        # #     i+=1
        # #     j+=1

        # while left<right:
        #     mid=numbers[left]+numbers[right]
        #     if mid==target:
        #         return [left+1,right+1]
        #     elif mid<target:
        #         left+=1
        #     else:
        #         right-=1





















        left=0
        right=len(numbers)-1
        while left<right:
            mid=numbers[left]+numbers[right]
            if mid==target:
                return left+1,right+1
            elif mid<target:
                left+=1
            else:
                right-=1
                