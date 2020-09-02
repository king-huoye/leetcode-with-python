class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s=""
        for i  in zip(*strs):#将字符解压，变成若干个个集合
            if len(set(i))==1:#通过集合的去重性
                s+=i[0]
            else:
                break
        return s











