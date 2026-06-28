import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            hour=0
            for pile in piles :
                hour+=math.ceil(float(pile)/mid)
            if hour<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        