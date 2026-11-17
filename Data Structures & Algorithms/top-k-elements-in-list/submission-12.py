class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     

    
        #Input: integer array of nums and k -> the most frequent elements within the array
        #Output: a unique set of elements that occur k times

        #Test cases:
        #answer is always unique
        #let's say k = 1
        #but [1,1,2,2] --> these elements both occur twice, would we return both or just one
        #if k is greater than the length of the array what would we return?


        #hashMap: store counts of each element, return k largest counts?
        #minHeap: but I forgot how to do this :(

        hashMap = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        #loop through to get the k largest counts
        sortedHashMap = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
        result = set()
        k_count = 0

        for i in sortedHashMap:
            if k_count < k:
                result.add(i)
                k_count += 1

        return list(result)
        