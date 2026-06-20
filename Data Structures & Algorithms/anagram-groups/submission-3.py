class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Understand the code
        #[["act", "pots", "tops", "cat", "stop", "hat"]]

        hashMap = {}
        #{occurrences count: list}

        #looping through the array
        for i in strs:
            #looping through the words
            occurrences = {}
            #{character:frequency}
            for c in i:
                if c not in occurrences:
                    occurrences[c] = 1
                elif c in occurrences:
                    occurrences[c] += 1
            #create a tuple with the occurrences
            key = tuple(sorted(occurrences.items()))

            if key in hashMap:
                hashMap[key].append(i)
            elif key not in hashMap:
                hashMap[key] = [i]

        result = [] 
        for k in hashMap:
            result.append(hashMap[k]) 
        return result          


    #go through an example
