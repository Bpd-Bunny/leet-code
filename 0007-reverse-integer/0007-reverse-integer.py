class Solution:
    def reverse(self, x: int) -> int:
        n=0
        i=1
        if x<0:
            x=x*(-1)
            i=-1
        while x!=0:
            a=x%10
            n=n*10+a
            x=x//10
        if n < -2**31 or n > 2**31 - 1:
            return 0
        else:
            return n*i