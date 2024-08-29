class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==1 or s==s[::-1]: return s
        def expand(s,i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]

        max_str=''
        for i in range(0,len(s)):
            if len(max_str)<len(expand(s,i,i)):
                max_str=expand(s,i,i)
            if len(max_str)<len(expand(s,i-1,i)):
                max_str=expand(s,i-1,i)

        return max_str
