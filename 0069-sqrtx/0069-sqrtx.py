class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x//2 if x!=1 else x
        while l<=r:
            m = l+ (r-l)//2
            if m*m<=x and (m+1)*(m+1)>x:
                return m
            elif m*m>x:
                r=m-1
            else:
                l=m+1