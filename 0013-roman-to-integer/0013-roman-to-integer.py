class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pair = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = 0
        for i in range(len(s)):
            curr = pair[s[i]]
            next_val = pair[s[i+1]] if i+1 < len(s) else 0

            if curr<next_val:
                n -= curr
            else:
                n += curr
        return n
            