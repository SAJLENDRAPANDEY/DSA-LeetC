class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}
        res=[]
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        
        sorted_v=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for ch ,count in sorted_v:
            res.append(ch*count)
        return "".join(res)