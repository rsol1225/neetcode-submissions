class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #understand
        #input: list of strings
        #output: a list of sublists of anagrams
        #[[words that are anagrams], [words that are anagrams]]

        #anagram: string that contains the exact same characters as another string
        '''
        bat and tab would be anagrams
        '''

        #test cases:
        #empty string --> is that considered an anagram? yes
        

        #Matching section
        #hashMap: [counts] : [words]
        #loop through the list
            #for each word get each of the counts
                #create dictionary for the counts
                #order the word counts
                #check if the word counts exist: add it to the hashMap values
                #if it doesn't
                    #which then becomes a new key in the hashMap
                    #and we want to add the word as one of the values
        #return [dict.values()]
                    
        #brute force:
         #loop through each word and compare to everything else in the list: O(n^2)

        hashMap = {}

        for s in strs:
            counts = {} #{character:count in a word}

            for c in s:
                if c in counts:
                    counts[c] += 1
                else:
                    counts[c] = 1
        
            key = tuple(sorted(counts.items()))
            if key in hashMap:
                hashMap[key].append(s)
            else:
                hashMap[key] = []
                hashMap[key].append(s)

        return list(hashMap.values())


        #["hi", "ih", "bye"]

