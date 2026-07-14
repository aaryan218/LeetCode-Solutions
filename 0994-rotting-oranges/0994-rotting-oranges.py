class Solution(object):
    def orangesRotting(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        from collections import deque
        m,n=len(g),len(g[0])
        q,f=deque(),0
        for i in range(m):
            for j in range(n):
                if g[i][j]==2:q.append((i,j))
                if g[i][j]==1:f+=1
        t=0
        while q and f:
            for _ in range(len(q)):
                x,y=q.popleft()
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    a,b=x+dx,y+dy
                    if 0<=a<m and 0<=b<n and g[a][b]==1:
                        g[a][b]=2
                        f-=1
                        q.append((a,b))
            t+=1
        return t if not f else -1