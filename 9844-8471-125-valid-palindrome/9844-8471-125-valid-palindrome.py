class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for i in s:
            if i.isalnum() :
                a+=i
        a=a.lower()
        n=len(a)
        for i in range(n//2):
            if a[i]!=a[-1-i]:
                return False
        return True