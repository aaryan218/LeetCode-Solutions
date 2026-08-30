class Solution:
    def minimumDeletions(self, nums):
        madx = float('-inf')
        midx = float('inf')
        max_idx = -1
        min_idx = -1

        for i in range(len(nums)):
            if nums[i] > madx:
                madx = nums[i]
                max_idx = i

            if nums[i] < midx:
                midx = nums[i]
                min_idx = i

        c1 = len(nums) - (abs(max_idx - min_idx) - 1)


        c2 = max(max_idx, min_idx) + 1

        c3 = len(nums) - min(max_idx, min_idx)


        return min(c1, min(c2, c3))