class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        n = len(s)
        dp = [[-1] * n for _ in range(n)]  

        max_len, sp = 0, 0

        for i in range(n):
            for j in range(i, n):
                if self.isPalin(s, i, j, dp):
                    length = j - i + 1
                    if length > max_len:
                        max_len = length
                        sp = i
        return s[sp:sp + max_len]

    def isPalin(self, s, i, j, dp):
        if dp[i][j] != -1:
            return dp[i][j] == 1
        if i >= j:
            dp[i][j] = 1
            return True
        if s[i] != s[j]:
            dp[i][j] = 0
            return False
        if self.isPalin(s, i + 1, j - 1, dp):
            dp[i][j] = 1
            return True
        else:
            dp[i][j] = 0
            return False