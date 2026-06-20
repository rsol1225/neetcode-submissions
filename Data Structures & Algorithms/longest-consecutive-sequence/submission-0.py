class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        longest_length = 0

        for n in nums:
            #that means this is the start of the subsequence
            if n-1 not in nums:
                #restart the calculation of the length
                length = 0
                while (n+length) in numSet:
                    length += 1
            
            longest_length = max(length,longest_length)
        
        return longest_length