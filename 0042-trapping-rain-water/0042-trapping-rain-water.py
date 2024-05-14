class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        l_max = [0]*n
        r_max = [0]*n
        for i in range(0,n):
            j=-i-1
            l_max[i] = max(l_max[i-1], height[i])
            r_max[j] = max(r_max[j+1], height[j])

        for i in range(0,n):
            water += min(l_max[i], r_max[i]) - height[i]
        return water