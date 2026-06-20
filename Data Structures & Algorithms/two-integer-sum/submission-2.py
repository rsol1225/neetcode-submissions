class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashMap = {}
        for i in range(0, len(nums)):
            number_needed = target - nums[i]
            if number_needed in hashMap:
                return [hashMap[number_needed], i]
            else:
                hashMap[nums[i]] = i
     
