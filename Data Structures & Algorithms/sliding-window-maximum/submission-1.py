class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #edge cases
        if k > len(nums):
            return []
        
        dq = deque() #keeps track of the indices
        result = [] #appends the max to this array

        #[1,4,5]
        #right pointer to move  along in the array
        #need to figure out the start

        for right in range(0, len(nums)):
            start = right - k + 1

            #remove from front if it's outside the window
            if dq and dq[0] < start:
                dq.popleft()
            
            #pop from back while back is smaller than current
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)

            if right >= k-1:
                result.append(nums[dq[0]])
        
        return result
                

