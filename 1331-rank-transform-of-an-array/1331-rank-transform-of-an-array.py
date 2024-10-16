class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num=list(set(arr.copy()))
        num.sort()

        dic = {}
        rank = 0
        for i in num:
            rank+=1
            dic[i]=rank
        
        n=[]
        for i in arr:
            n.append(dic[i])
        return n