class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        boxes = list(boxes)  
        for i in range(n):
            boxes[i]=int(boxes[i])
        right = [0]*n
        left = [0]*n
        ones = 0 if boxes[-1] != 1 else 1
        for i in range(n-2,-1,-1):
            right[i] += right[i+1] + ones
            if boxes[i]==1:
                ones+=1
        ones = 0 if boxes[0] != 1 else 1
        for i in range(1,n):
            left[i] += left[i-1] + ones
            if boxes[i]==1:
                ones +=1
        l=[]
        for i in range(n):
            l.append(right[i]+left[i])
        return l