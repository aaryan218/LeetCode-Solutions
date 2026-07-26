class MyStack(object):

    def __init__(self):
        self.li=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.li.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        a = self.li.pop()
        return a
       

    def top(self):
        """
        :rtype: int
        """
        a = self.li.pop()
        self.li.append(a)
        return a

        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.li) == 0
            
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()