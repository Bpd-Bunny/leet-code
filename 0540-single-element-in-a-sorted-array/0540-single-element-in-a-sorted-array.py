class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        if len(nums)==1: return nums[0]
        if nums[0]!=nums[1]: return nums[0]
        if nums[-1]!=nums[-2]: return nums[-1]
        
        while l<=r:
            m=l+(r-l)//2
            if nums[m]!=nums[m-1] and nums[m]!=nums[m+1]:
                return nums[m]
            
            if nums[m]==nums[m-1]:
                if (m-1-l)%2!=0:
                    r=m-2
                else: l=m+1
            else:
                if (r-m+1)%2!=0:
                    l=m+2
                else: r=m-1