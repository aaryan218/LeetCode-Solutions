class Solution:
    def reverse(self, x: int) -> int:
        if x<=-(1<<30) or x>=(1<<30)-1:
            return 0
            
        if x>0:
            a=int(str(x)[::-1])
            if  a>(1<<30)-1:
                return 0
            return int(str(x)[::-1])
        else:
            a=-int(str(-x)[::-1])
            if a<-(1<<30):
                return 0
            return -int(str(-x)[::-1])
