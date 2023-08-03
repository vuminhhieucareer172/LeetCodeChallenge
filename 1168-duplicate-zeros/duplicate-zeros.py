class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0
        while index < len(arr) - 1:
            if arr[index] == 0:
                for i in range(len(arr) - 1, index + 1, -1):
                    arr[i] = arr[i-1]
                arr[index + 1] = 0
                index += 1
            index += 1
        print(arr)