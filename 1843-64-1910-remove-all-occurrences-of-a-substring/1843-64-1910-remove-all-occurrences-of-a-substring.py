class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n=len(part)
        while s.find(part)!=-1:
            print(s)
            idx = s.find(part) 
            new_text = s[:idx]+s[idx+n:]
            s=new_text
        return s
        