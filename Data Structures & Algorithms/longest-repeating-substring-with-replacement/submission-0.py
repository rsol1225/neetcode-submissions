class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Input: s
        #output: return the length of the logenst substring which contains one distinct character

        #choose up to K character of the string and replace them with any other uppercase English Character

        #Algorithm:
            #can i turn everything in this window into the most 
            #frequent character?
            #keep track of the max Length
            #XYYX
                #window_size = right - left + 1
                #length = window_size - 
        #XYYX

        

        hashMap ={} #value:counts, counts is the frequency of the character
        maxLength = 0
        maxFrequency = 0
        left = 0 

        for right in range(0, len(s)):
            #get the max frequency of the current string
            if s[right] not in hashMap:
                hashMap[s[right]] = 1
            else:
                hashMap[s[right]] += 1

            maxFrequency = max(maxFrequency, hashMap[s[right]])
            window_size = right - left + 1
            replacements = window_size - maxFrequency

            #need the invariant here
            if replacements > k:
                hashMap[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right-left+1)
        
        return maxLength


