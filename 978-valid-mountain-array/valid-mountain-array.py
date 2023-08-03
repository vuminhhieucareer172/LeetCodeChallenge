class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
            slow = 0
            fast = 1
            change = 0
            while fast <= len(arr) - 1:
                if arr[slow] < arr[fast]:
                    slow += 1
                    fast += 1
                    if change == 0:
                        continue
                    else:
                        return False
                elif arr[slow] > arr[fast]:
                    if slow == 0:
                        return False
                    slow += 1
                    fast += 1
                    if change == 0:
                        change += 1
                    elif change == 1:
                        continue
                else:
                    return False
            if change == 1:
                return True
            return False