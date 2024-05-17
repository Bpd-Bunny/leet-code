class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n= len(nums)
        pos=[]
        neg=[]
        for i in range(0,n):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        a=b=0
        for i in range(0,n):
            if i%2==0:
                nums[i] = pos[a]
                a +=1
            else:
                nums[i] = neg[b]
                b += 1

        return nums
        