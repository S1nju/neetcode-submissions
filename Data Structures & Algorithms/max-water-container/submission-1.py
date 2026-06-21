class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0

        for i in range(int(len(heights))):
            for j in range(i+1,int(len(heights))):
                area = min(heights[i],heights[j])*(j-i)
                max_area = max(area,max_area)
        return max_area
        