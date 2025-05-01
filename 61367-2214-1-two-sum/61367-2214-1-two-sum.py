class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(0,len(nums)):
            d[nums[i]]=i
        for i in range(0,len(nums)):
            y = target-nums[i]
            if y in d and d[y]!=i :
                return [i,d[y]]
