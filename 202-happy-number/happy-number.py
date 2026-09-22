class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=set()
        while n!=1:
            t=0
            for d in str(n):
                t+=int(d)**2
            if t in s:
                return False
            s.add(t)
            n=t
        return True


        