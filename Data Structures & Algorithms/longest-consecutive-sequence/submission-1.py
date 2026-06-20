class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Understand the problem
        #Input nums = [2,20,4,10,3,4,5]
        #Output: 4
        #Do repeats count?
        #is nums sorted?

        #Patterns
        #Sort the numbers, and then loop through
        #O(nlogn) + O(n)

        #Better: O(n)

        #nums = [2,20,4,10,3,4,5]

        #Possible solutions
        #Sort the array and then find the consecutive with a counter (O(nlogn) + O(n))
        
        #Possible solution

        #each sequence doesn't have a left number
        #1,2,3,4,100
        numSet = (nums) #sets have a O(1) look up time
        length = 0
        longest_length = 0

        for n in nums:
            if n-1 not in numSet:
                #start of sequence
                length = 0
                while(n+length) in numSet:
                    length += 1
            longest_length = max(length, longest_length)

        return longest_length

