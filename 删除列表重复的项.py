class List(object):
    pass
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = set(nums)  # 变成集合
        nums.clear()  # 清空列表
        a = list(a)  # 集合变列表
        nums.extend(a)  # 将集合添加到列表
        nums.sort()
        return len(nums)









