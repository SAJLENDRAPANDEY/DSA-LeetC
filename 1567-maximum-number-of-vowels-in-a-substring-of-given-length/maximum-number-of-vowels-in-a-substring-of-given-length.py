class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        x='aeiou'
        count=0
        
        for i in range(k):
            if s[i] in x:
                count+=1
        max_count=count
        for i in range(k,len(s)):
            if s[i-k] in x:
                count-=1
            if s[i] in x:
                count+=1
            max_count=max(max_count,count)
        return max_count
            



                
        