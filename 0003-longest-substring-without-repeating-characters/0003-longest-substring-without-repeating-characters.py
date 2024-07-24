class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0 if len(s)==0 else 1
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                if s[j] not in s[i:j]:
                    max_len = max(max_len,len(s[i:j+1]))
                else:
                    break
        return max_len
        