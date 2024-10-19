class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = l + (r-l)//2
            if nums[m]==target:
                return m
           # check that left of mid is sorted or not
            elif nums[l] <= nums[m]:
                # target is present or not
                if nums[l]<=target and nums[m]>target :
                    r=m-1
                else: 
                    l=m+1
            # else Right of mid is sorted  
            else:
                # target is present or not
                if nums[m]<target and nums[r]>=target:
                    l=m+1
                else:
                    r=m-1
        return -1