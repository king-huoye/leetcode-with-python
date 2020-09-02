class Solution:
    def plusOne(self, nums):
        t = len(nums)
        sum = 0
        for i in range(t):
            sum += nums[i] * pow(10, t - 1 - i)

        num=[]
        sum += 1
        sum = str(sum)
        for i in sum:
            num.append(int(i))
        return num


