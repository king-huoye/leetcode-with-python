class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)#转为字符串
        if x==x[::-1]:#右边是后面开始
            return True
        else:
            return False

