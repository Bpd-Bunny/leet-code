class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(nums, start, end):
            if end - start <= 1:
                return 0
            mid = (start + end) // 2
            count = merge_sort(nums, start, mid) + merge_sort(nums, mid, end)
            j = mid
            for i in range(start, mid):
                while j < end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid
            nums[start:end] = sorted(nums[start:end])
            return count
            

        return merge_sort(nums, 0, len(nums))
