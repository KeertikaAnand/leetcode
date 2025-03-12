class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1=0
        p2=len(height)-1
        max_area=0
        while p1<p2:
            area = (p2 - p1) * min(height[p1], height[p2])
            max_area = max(max_area, area)
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        return max_area