class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Understanding
        # nums[i] + nums[j] == target i != j
        # input: an array of integers
        # returns the indicies i and j that add up to the target

        # Test cases
            # empty array
        
        # Example [3,4,5,6] target = 7
        # 7-3, so we need a number with a 4
        # 7-4, so we check for a 3 in the hashmap
        # 7-5, so we check for a 2 in the hashmap
        # hashMap will have the number needed and the value will be the index

        #example: [3,4,5,6] and target = 7
        #hashMap: nN = 7-3 = 4
        # 4 is not in the hashMap
        # add {3:1}
        # now we hae encountered 3
        # 7-4=3
        #we have a solution

        #{4,5,6} and target = 10
        # hashMap = {4:0}
        # 10-5 = 5
        # hashMap = {4:0, 5:1}
        # 10 - 6 = 4


        hashMap = {}

        for i in range(0,len(nums)):
            numberNeeded = target - nums[i]

            if numberNeeded not in hashMap:
                hashMap[nums[i]] = i
            elif numberNeeded in hashMap:
                index = hashMap[numberNeeded]
                if index != i:
                    return [index, i]
        return []