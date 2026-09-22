class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        freq={}
        res=[]
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        length=0
        odd=False

        for ch in freq:
            if freq[ch]%2==0:
                length+=freq[ch]
            else:
                length+=freq[ch]-1
                odd=True
        if odd:
            length+=1
        return length

