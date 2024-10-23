class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # print(chr(122))
        l=0
        r=len(letters)-1
        res=0
        while l<=r:
            m=l+(r-l)//2
            if letters[m]>target:
                res = m
                r=m-1
            else: 
                l=m+1
        if res!=0:
            return letters[res]
        else: 
            return letters[0]