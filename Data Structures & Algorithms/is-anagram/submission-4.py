class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Understanding
        ''' Ask clarifying questions and use examples to understand what the interviewer wants out of this problem
Choose a “happy path” test input, different than the one provided, and a few edge case inputs. Verify that you and the interviewer are aligned on the expected inputs and outputs. '''

#Brute force
#HashMap dictonary, loop through and [letter] : [count]
                    #at the end make sure both have the same amount of keys and count
                    #Time complexity: O(n)
                    #Space complexity O(n)

#Sort alphabetically -> O(nlogn), loop through s and t and make sure each character is the same
                        #O(nlogn)
                        #check if their lengths are the same
                        #if not loop through and t, O(n)
                        #O(nlogn) + O(n)
#Plan
    #check length, return false if the lengths arent the same
    #hashMap = {}

    #loop s, add to hashMapS
    #loop t, subtract from hashMap and if letter not in s, return false

    #loop through and check all the counts are 0
        #if the count is > 0, return false
    
        hashMap = {}
        if len(s) != len(t):
            return False
        
        for key in s:
            if key not in hashMap:
                hashMap[key] = 1
            else:
                hashMap[key] += 1
        
        for key in t:
            if key in hashMap:
                hashMap[key] -= 1
            if key not in hashMap:
                return False
        
        for key in hashMap:
            if hashMap[key] != 0:
                return False
        return True
    


    