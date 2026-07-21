class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # min_n=float('inf')
        # max_n=0
        # for num in  prices:
        #     min_n=min(min_n,num)

        #     profit=num-min_n
        
        #     max_n=max(max_n,profit)
        # return max_n


























        min_p=float('inf')
        max_p=0
        for num in prices:
            min_p=min(min_p,num)
            profit=num-min_p
            max_p=max(max_p,profit)
        return max_p
        