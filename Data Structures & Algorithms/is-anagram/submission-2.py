class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Understanding 
            #input: two string s and t
            #output: true or false, are they anagrams or not

            #how to determine if they are anagrams:
            #1. contain the exxact same characters, but order can be different

            #edge cases:
            #if they contain the exact same characters, they must have the same length
            #if they both are empty strings, that means they match

        #Matching
            #Hashmap solution: 
            #I can use a hashmap for both strings, keep track of the counts
            # and loop through and compare the counts 

            
            
            if len(s) != len(t):
                return False
            
            count_s = {}
            count_t = {}

            for i in s:
                if i not in count_s:
                    count_s[i] = 1
                if i in count_s:
                    count_s[i] += 1
            
            for j in t:
                if j not in count_t:
                    count_t[j] = 1
                if j in count_t:
                    count_t[j] += 1
            
            if len(count_t) != len(count_s):
                return False

            
            return count_t == count_s
            
        
            

        
        