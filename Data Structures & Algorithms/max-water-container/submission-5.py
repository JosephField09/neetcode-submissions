class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        m = 0
        while l <= r:
            diff = r - l
            water = min(heights[r], heights[l]) * diff
            m = max(m, water)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return m