class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left, right = n, n
        ans = []
        def dfs(left, right, path):
            if not left and not right:
                ans.append(path)
                return
            if left :
                # path += "("
                dfs(left - 1, right, path + "(")
            if right > left:
                # path += ")"
                dfs(left, right-1, path + ")")

        dfs(left, right, "")

        return ans