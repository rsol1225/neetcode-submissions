class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #Understanding 
        #Output: return true if any value appears more than once
        #Input: a list of integers

        #Test cases:
        #empty list -> return false b/c no matching
        #[1,1,2,2,3,3] -> also returns false

        #Matching
        #Brute force:
            #sort the elements O(nlogn)
            #loop through the list and keep a counter
            #each time we get a new element counter switches back to 0
            # if counter > 1, we return false
            # O(n)
            #time complexity: O(nlogn) + O(n)
        #Hashmap:
            #lookup time: O(1)
            #Memory O(n)
            #intialize a hashmap
            #loop through the input list
                # then every time you encounter a number, if it's not in the hashmap
                # you add it to the hashmap and increase it's value 
                # if it is in the hashmap, then you return false
        
        hashmap = {}

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            elif n in hashmap and hashmap[n] == 1:
                return True
        return False

        

