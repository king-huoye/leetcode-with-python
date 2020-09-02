class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        s=s.split()#切割字符串
        return len(s[-1]) if s else 0





