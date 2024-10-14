class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        ans = 0
        for i in nums:
            if freq == 0:
                ans = i
            if ans == i:
                freq += 1
            else:
                freq -=1
        return ans        
        
        
        
        
        
        
        
    
        
        
        
        
        
        # nums.sort()
        # curr=0
        # if len(nums)==1:
        #     return nums[0] 
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         curr += 1
        #     else:
        #         curr = 1
                
        #     if curr >= len(nums)//2:
        #         return nums[i]
        