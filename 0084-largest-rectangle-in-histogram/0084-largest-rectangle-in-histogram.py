class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        s, ans = [], 0
        for i in range(len(heights) + 1):
            h = heights[i] if i < len(heights) else 0
            while s and heights[s[-1]] >= h:
                x = heights[s.pop()]
                ans = max(ans, x * (i if not s else i - s[-1] - 1))
            s.append(i)
        return ans