class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n-1
        max_area = 0
        while l<r:
            width =r-l
            h = min(height[l],height[r])
            area = width*h
            max_area = max(max_area,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area