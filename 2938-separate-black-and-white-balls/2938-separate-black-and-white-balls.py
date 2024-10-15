class Solution:
    def minimumSteps(self, s: str) -> int:
        hit = 0
        steps = 0
        for i in s:
            if i=='1':
                hit+=1
            else :
                steps +=hit
        return steps