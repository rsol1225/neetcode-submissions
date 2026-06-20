class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #Understanding:
        #1. If any value appears more than once -> return true
        #2. Does the array come in sorted order? 

        #Matching:
        #1. Hashmap -> count the number of occurences for each integer O(n)
        #2. Sorting -> sort the array, loop through and if you encounter the previous number, return false
            # O(nlogn)
        
        #Pseudocode: hashmap

        #hashmap
        #loop though the array
            # store it in the hashmap if it isn't there
            # if something is already in the array: true
        #return false

        occurenceMap = {} #value:count
        for i in range(0, len(nums)): #O(n)
            if nums[i] in occurenceMap: #O(1)
                return True
            else:
                occurenceMap[nums[i]] = 1
        return False