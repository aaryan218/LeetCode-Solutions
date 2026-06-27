# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def verticalTraversal(self, root):
        d, q = defaultdict(list), deque([(root, 0, 0)])

        while q:
            n, r, c = q.popleft()
            d[c].append((r, n.val))

            if n.left: 
                q.append((n.left, r + 1, c - 1))

            if n.right: 
                q.append((n.right, r + 1, c + 1))
        return [[v for _, v in sorted(d[c])] for c in sorted(d)]