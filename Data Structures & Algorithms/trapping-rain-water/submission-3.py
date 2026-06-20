class Solution:
    def trap(self, height: List[int]) -> int:
        

        #Understanding
        #Input: array of non-negative integers
        #Output:maximum area of water that can be trapped between the bars

        #[0,2,0,3,1,0,1,3,2,1]
        #there has to be space between the heights
        
        left, right = 0, len(height)-1
        rightMax = height[right]
        leftMax = height[left]
        res = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        
        return res




        #iteration 1: 0
        #left = 1
        # right = 2

        #iteration#2: 
        #currentArea = 2

        #iteration #3"
        #left = 1
        #right = 3
        #maxArea = 2
        #left = 3
        #right = 4

        #iteration #4
        #currentArea = 2
