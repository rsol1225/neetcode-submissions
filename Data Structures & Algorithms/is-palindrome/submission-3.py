class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #Input: string
        #Output: true or false depending on if it's a palindrome

        #Example: "was it a car or a cat I saw?"

        #All letters and numbers are allowed, what spaces?

        #Match:
        #Ignore all characters that aren't alphanumeric
        #Copy the string, reverse and compare, memory O(n)
        #Two pointer solution, memory at O(1) and O(n)

        #Example: "    abcdc?ba"
        #left = 0
        #right = len(s) - 1

        #while left < right:
            #if the left character is not  alphanumeric:
                #left += 1
            #if the right character is not alphanumeric
                #right -= 1
            #elif left character == right character:
                #continue
                #left += 1
                # right -=1
            #elif left character != right character
                # return false
        #return true


        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalnum() == False:
                left += 1
            elif s[right].isalnum() == False:
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
        
        return True