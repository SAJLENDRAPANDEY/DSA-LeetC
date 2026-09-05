class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for token in tokens:
            if token in "+-*/":
                a=stack.pop()
                b=stack.pop()
                
                if  token=="+":
                    res=b+a
                elif token=="-":
                    res=b-a
                elif token=="*":
                    res=b*a
                else:
                    res=int(float(b)/a)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]
        