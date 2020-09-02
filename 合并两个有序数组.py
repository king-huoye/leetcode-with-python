class List:
    pass
class Solution:
    def merge(self, nums1,nums2,m,n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        for i in range(n):
            nums1.append(nums2[i])
        return nums1.sort()