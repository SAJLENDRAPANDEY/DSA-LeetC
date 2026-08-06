class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # freq={}
        # for num in nums:
        #     freq[num]=freq.get(num,0)+1
        # sorted_fre=sorted(freq.items(),key=lambda x:x[1] ,reverse=True)
        # res=[]
        # for x in range(k):
        #     res.append(sorted_fre[x][0])
        # return res
























        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        sorted_num=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_num[i][0])
        return res