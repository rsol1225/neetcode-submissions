from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Using a min heap
        #log of nlogk

        
        hashMap = {}

        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            elif i not in hashMap:
                hashMap[i] = 1
        #Creates a counter: (key, frequency)
        
        #Creating an array of len(nums)+1 each index is associated with a value
        buckets = [0] * (len(nums)+1) # need to add one b/c of 0 indexing

        for key, value in hashMap.items():
            if buckets[value] == 0:
                buckets[value] = [key]
            else:
                buckets[value].append(key)

        result = []
        for i in range(len(nums),0,-1):
            if buckets[i] != 0:
                result.extend(buckets[i])
            if len(result) == k:
                break
        return result

        #Time complexity: O(n) + O(n) + O(n), has a time compelxity of O(n)

        