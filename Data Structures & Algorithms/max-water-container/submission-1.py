class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0

        l, r = 0, len(heights) - 1

        while l < r:
            length = r - l
            volume = length * min(heights[l], heights[r])
            max_volume = max(volume, max_volume)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_volume