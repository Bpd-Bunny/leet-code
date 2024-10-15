class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # create a freq arr to store the reminder from 0 to k-1
        freq=[0]*k
        for i in arr:
            freq[((i % k) + k) % k ] +=1

        # check the 0th index is even val or not
        if freq[0]%2!=0:
            return False
        # check the pairing index is even or not
        for i in range(1,(k//2)+1):
            if freq[i]!=freq[k-i]:
                return False
        return True