class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        a = n-1
        for i in range(n-1,-1,-1):
            if nums[i]>=nums[a]:
                a = i
            else:
                break
        a-=1
        if a==-1:
            nums.sort()
            pass
        
        for i in range(n-1, a,-1):
            if nums[i]>nums[a]:
                nums[i], nums[a] = nums[a], nums[i]
                break

        arr = nums[a+1:]
        arr.sort()
        for i in arr:
            nums[a+1]=i
            a+=1