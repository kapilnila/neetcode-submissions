class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1

        max_val=0

        while i<j:
            max_val=max(max_val,(j-i)*min(heights[i],heights[j]))
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return max_val