class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pi=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pi=i
                break
        if pi==-1:
            nums.reverse()
            return
        for i in range(n-1,pi,-1):
            if nums[pi]<nums[i]:
                nums[pi],nums[i]=nums[i],nums[pi]
                break
        nums[pi+1:] = reversed(nums[pi+1:])
       