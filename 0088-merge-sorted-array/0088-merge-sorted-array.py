class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = 0
        while m <len(nums1) :
            nums1[m] = nums2[i]
            i+=1
            m+=1
        nums1.sort()










        # while i<m+n and j<n:
        #     if nums1[i]==0 or nums1[i]>nums2[j]:
        #         nums1[i], nums2[j] = nums2[j], nums1[i]
        #         i+=1
        #     else:
        #         j+=1
        # print(nums1)
        # print(nums2)