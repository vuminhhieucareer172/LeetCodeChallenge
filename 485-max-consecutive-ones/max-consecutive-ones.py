class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                result.append(count)
                count = 0
            if i == len(nums) - 1:
                result.append(count)
        return max(result)