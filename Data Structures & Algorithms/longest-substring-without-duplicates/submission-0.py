class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Understand the problem
        #input: s
        #output: the length of the longest substring without duplicates

        #edge cases:
        # empty string -> what do I return
        # 1 element string -> return length 1

        #Approaches:
        #Brute force: generate all substrings, and then go through each one to find one without and repeating characters
        #Sliding window approach: 
        #we have a window that we shrink and expand depending on if we see duplicates or not
        #time complexity: O(n)

        longestSubstring = 0
        characters = set()
        left = 0 #so we can keep shrinking the window until we find duplicates
        #need to keep track of the current length
      
        for c in range(0, len(s)):
            
            #let's shrink the window when we see a duplication
            while s[c] in characters and c < len(s):
                characters.remove(s[left])
                left += 1
                
            characters.add(s[c])
            longestSubstring = max(longestSubstring, c-left+1)
        
        return longestSubstring
            
