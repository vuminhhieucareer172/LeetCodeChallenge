class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        clone = heights.copy()
        clone.sort()
        for i in range(len(heights)):
            if heights[i] != clone[i]:
                count += 1
        return count