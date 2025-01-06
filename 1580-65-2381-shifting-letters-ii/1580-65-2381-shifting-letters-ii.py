class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        l=[0]*(n+1)
        for start, stop, step in shifts:
            if step ==1:
                l[start]+=1
                l[stop+1] -=1
            else:
                l[start]-=1
                l[stop+1] +=1
        curr = 0
        a=''
        for i in range(n):
            curr += l[i]
            ind = (ord(s[i])+curr-97)%26
            a += chr(97+ind)

        return a