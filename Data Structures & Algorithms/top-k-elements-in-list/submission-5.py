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
        
        buckets = [0] * (len(nums)+1)

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

        