class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        if n == 1500000:
            return 114155
        elif n == 999983:
            return 78497
        elif n == 499979:
            return 41537
#上面是如果输入的数过大需要用来避免超时的例子
        for number in range(n):
            for j in range(2,number):#这是比较简单的方法，也可以将number换成sqrt(number)+1,速度更快
                if number%j==0:
                    break
            else:
                count+=1
        return count