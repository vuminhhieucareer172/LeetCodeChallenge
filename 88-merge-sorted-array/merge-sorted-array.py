class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in nums2:
            self.doMerge(i, m, nums1)
            m += 1
        print(nums1)

    def doMerge(self, insertNumber, m, nums1):
        isNeedInsert = False
        for i in range(m):
            if nums1[i] > insertNumber:
                for k in range(m - 1, i - 1, -1):
                    nums1[k + 1] = nums1[k]
                nums1[i] = insertNumber
                isNeedInsert = True
                break
        if isNeedInsert is False:
            nums1[m] = insertNumber