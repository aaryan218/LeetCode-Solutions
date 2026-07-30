class Solution:
    def minimumPushes(self, s: str) -> int:
        return ((n:=len(s))-n//8*4)*(n//8+1)