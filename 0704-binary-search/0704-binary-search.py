class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # using recursion
        # def binarySearch(l, r, num, target):
        #     if l<= r:
        #         m = l + (r-l)//2
        #         if target > num[m]:
        #             return binarySearch(m+1,r,num,target)
        #         elif target < num[m]:
        #             return binarySearch(l,m-1,num,target)
        #         else: return m
        #     return -1
        # return binarySearch(0,len(nums)-1,nums,target)
        
        # without Recurrision
        l =0
        r = len(nums)-1
        while l <= r:
            m = l + (r -l)//2 
            if target > nums[m]:
                l = m +1
            elif target < nums[m]:
                r = m-1
            else: 
                return m
        return -1
