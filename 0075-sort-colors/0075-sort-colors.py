from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dic = Counter(nums)
        k=0
        for i in range(len(nums)):
            if dic[0]!=0:
                nums[k]=0
                dic[0]-=1
            elif dic[1]!=0:
                nums[k]=1
                dic[1]-=1
            else:
                nums[k]=2
                dic[2]-=1
            k+=1