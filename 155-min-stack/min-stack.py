class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.MinStack=[]
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        if not self.MinStack or value<=self.MinStack[-1]:
            self.MinStack.append(value)

        

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return 
        if self.stack[-1] == self.MinStack[-1]:
            self.MinStack.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack is None:
            return 
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.MinStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()