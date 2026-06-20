class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #Understand the problem

        #Given a list of heights: these bars form containers
        #I can pick 2 bars: ground*7*7 = 49
                            #if the height is shorter than only the shortest height will fit
        
        
        
        left = 0
        right = len(heights) -1
        maxArea = 0

        while left < right:
            smallest_height = min(heights[left],heights[right])
            current_maxArea = (right-left)*smallest_height
            maxArea = max(current_maxArea, maxArea)

            if heights[left] == smallest_height:
                left += 1
            elif heights[right] == smallest_height:
                right -= 1
        
        return maxArea
            