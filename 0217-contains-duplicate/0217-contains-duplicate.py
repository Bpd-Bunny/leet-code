class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = list(set(nums))
        if len(n)!=len(nums):
            return True
        else: return False 