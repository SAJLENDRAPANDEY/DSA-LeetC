class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x="{[("
        stack=[]
        for ch in s:
            if ch in x:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top=stack[-1]
                if (ch==')' and top!='(') or \
                (ch=='}' and top!='{') or \
                (ch==']' and top!='['):
                    return False
                stack.pop()
        return len(stack)==0
