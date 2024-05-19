class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        i = 0
        j=n-1
        while i<j:
            minh = min(height[i],height[j])
            tarea = minh*(j-i)
            area = max(tarea, area)
            if height[i] <= height[j] :
                i += 1
            else: 
                j -= 1
        return area