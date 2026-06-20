class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        #Understand:
        #1. Input: array of strings
        #2. Output: an array with all anagrams grouped in sublists

        
        #Other questions:
        #1. What if there is only 1 input? 
        #2. Does lowercase/uppercase matter?

        #Matching

        #loop through the list of strings
        hashMap = {}
        for s in strs:
            #loop through each string
            #keeping track of the occurences
            occurrences = {}
            for i in s:
                #count the occurrences
                if i not in occurrences:
                    occurrences[i] = 1
                if i in occurrences:
                    occurrences[i] += 1
            #check to see if those occurrences are in the hashmap
            key = tuple(sorted(occurrences.items()))
            if key not in hashMap:
                hashMap[key] = []
                hashMap[key].append(s)
            else:
                hashMap[key].append(s)
        
        return list(hashMap.values())


            

