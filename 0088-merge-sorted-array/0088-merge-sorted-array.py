class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ind=m+n-1 
        i = m-1
        j = n-1
        while (j>=0 and i>=0):
            if nums1[i]>=nums2[j]:
                nums1[ind]=nums1[i]
                ind-=1
                i-=1
            if nums2[j]>=nums1[i]:
                nums1[ind] = nums2[j]
                j-=1
                ind-=1
        while j>=0:
            nums1[ind]=nums2[j]
            ind-=1
            j-=1
