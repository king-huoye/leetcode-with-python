# class List(object):
#      pass
# class Solution:
#     def removeElement(self, nums: List, val: int) -> int:
#         len1=nums.count(val)
#         return len(nums)-len1
#
class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        n=nums.count(val)#统计要移除元素的个数
        for i in range(n):
            nums.remove(val)
        return len(nums)





