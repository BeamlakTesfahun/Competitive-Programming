class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1 
        result = 0
        while l < r:
            area = (r-l) * min(height[l], height[r])
            result = max(result,area)
            if height[l] < height[r]:
                l += 1
            # if height[l] == height [r] -> either l+=1 or r-=1 can be done
            # if height[l] > height[r]
            else:
                r -= 1
        return result
