class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Understanding: 
        #1. there's 2 strings, each with the same characters (order could be different)
        #2. Input: 2 strings
        #3. Output: true or false

        # Edge cases/special cases
        # length of both strings need to be the same
        if len(s) != len(t):
            return False
        
        count_occurences_s = {} # character: count
        count_occurences_t = {} # character: count

        for i in s:
            if i not in count_occurences_s:
                count_occurences_s[i] = 1
            else:
                count_occurences_s[i] += 1
        
        for j in t:
            if j not in count_occurences_t:
                count_occurences_t[j] = 1
            else:
                count_occurences_t[j] += 1
        
        for character in count_occurences_s:

            if character not in count_occurences_t:
                return False

            s_count = count_occurences_s[character]
            t_count = count_occurences_t[character]

            if s_count != t_count:
                return False
        
        return True

        
