class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s: return 0

        sign = -1 if s[0] == '-' else 1
        if s[0] in '+-': s = s[1:]

        res = 0
        for c in s:
            if not c.isdigit(): break
            res = res * 10 + int(c)

        res *= sign
        return max(-2**31, min(2**31 - 1, res))