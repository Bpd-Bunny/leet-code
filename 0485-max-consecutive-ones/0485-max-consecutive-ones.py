class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr +=1
            else:
                max_one = max(max_one, curr)
                curr = 0
        max_one = max(max_one, curr)
        return max_one