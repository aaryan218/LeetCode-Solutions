from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq=deque()
        res=[]
        depth=0

        if root:
            dq.append(root)

        while(dq):

            lvl=[]

            for _ in range(len(dq)):
                node=dq.popleft()

                lvl.append(node.val)

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

            if depth%2!=0:    
                lvl.reverse()     

            res.append(lvl)
            depth+=1

        return res