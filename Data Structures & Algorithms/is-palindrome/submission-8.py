class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while right > left:
            leftCharacter = s[left].lower()
            rightCharacter = s[right].lower()

            if leftCharacter.isalnum() == False:
                left += 1
                
            elif rightCharacter.isalnum() == False:
                right -= 1
                
            
            elif rightCharacter != leftCharacter:
                return False
            elif rightCharacter == leftCharacter:
                left += 1
                right -= 1
        
        return True