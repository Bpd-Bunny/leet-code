class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            m=l+ (r-l)//2
            coins= (m*(m+1))//2
            if coins==n:
                return m
            elif coins<n:
                l= m+1
            else: 
                r=m-1
        return r