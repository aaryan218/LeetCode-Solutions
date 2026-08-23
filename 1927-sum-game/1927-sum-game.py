class Solution:
    def sumGame(self, s: str) -> bool:
        n,f = len(s)//2,lambda t:sum(c!='?' and int(c) for c in t)
        return f(l:=s[:n])-f(r:=s[n:])!=(r.count('?')-l.count('?'))*9/2