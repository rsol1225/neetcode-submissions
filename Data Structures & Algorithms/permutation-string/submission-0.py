class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        hashMapS1 = {}

        for i in s1:
            if i not in hashMapS1:
                hashMapS1[i] = 1
            else:
                hashMapS1[i] += 1
        

        hashMapS2 = {}
        #build initial hashMap
        for j in range(0, len(s1)):
            if s2[j] not in hashMapS2:
                hashMapS2[s2[j]] = 1
            else:
                hashMapS2[s2[j]] += 1
        
        if hashMapS2 == hashMapS1:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            # add new char coming in on the right
            hashMapS2[s2[right]] = hashMapS2.get(s2[right], 0) + 1
            # remove old char going out on the left
            hashMapS2[s2[left]] -= 1
            if hashMapS2[s2[left]] == 0:
                del hashMapS2[s2[left]]
            left += 1
            
            if hashMapS2 == hashMapS1:
                return True
        

        return False


