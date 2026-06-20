class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Understanding
        #Input: given nums array and integer k
        #Output: returns the k most frequent element within the array, so the actual number

        #Testcases:
        #What if k is larger than the nums array?
        #Can k be 0?

        #Matching
        #Hashmaps: keep track of the counts of each element
                    #Could sort them
        #Sorting: sort the array, keep track of the counts


        hashMap = {}

        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            if i not in hashMap:
                hashMap[i] = 1
        
        #Loop through the hashMap
        sorted_items = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)

        k_count = 0
        result = set()
        for key,value in sorted_items:
            if k_count < k:
                result.add(key)
                k_count += 1
            elif k_count > k:
                break
           
        
        return list(result)



