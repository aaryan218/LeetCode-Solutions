class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        a=k
        for i in nums:
            if i==a:
                a+=k
        return a  