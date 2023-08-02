class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        time = nums.count(0)
        for i in range(time):
            nums.remove(0)
        for i in range(time):
            nums.append(0)