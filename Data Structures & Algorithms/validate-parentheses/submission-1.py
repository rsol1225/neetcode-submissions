class Solution:
    def isValid(self, s: str) -> bool:
        

        #Understanding
        #Input: a string consisting of (), {}, or []
            #Can be in any order as long as
            #Every open bracket is closed by the same type of close bracket
            #Every close bracket has a corresponding open bracket

        #Output: is s is valid
            #Valid criteria
            #every open bracket is closed by the same type
            #every close bracket has a corresponding open bracket
        
        #Test cases:
        # Open and close come in pairs, so if the length is odd, we can return false
        # One brackett: the length is odd so return false

        #Patterns:
        #1. stacks

        if len(s) <= 1:
            return False
        stack = []
        hashMap = {"}":"{",")":"(", "]": "[" }

        #logic, if we see a closing bracket take t
        #"[]"
        for i in s:
            #if we encounter closed bracked
            if i in hashMap.keys():
                if stack and stack[-1] == hashMap[i]:
                    stack.pop()
                else:
                    return False
            else: #since it's an opening bracket
                stack.append(i)
        
        if len(stack) > 0:
            return False
        return True
            
        


         