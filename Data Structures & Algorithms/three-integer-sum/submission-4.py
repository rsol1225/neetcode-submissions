class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        #Understand the problem:
        #Input: an integer array nums
        #Output: should not contain any duplicate triples
        #Each index is distinct
        #what happens if there's 1 number, do I return an empty array?



        #Matching
        #Brute force: loop 3 times, O(n^3)
        #Sorting and using two pointers

        #nums = [-1, 0, 1, 2, -1, -4]
        #sort it O(nlogn)

        #nums = [-4, -1, -1, 0, 1, 2]
        #Keep track of the previous number
        #case #1: i + left + right == target
                    # add to the result
        #case #2: i + left + right  < target and right < len(arr)-1:
                #right -= 1
        #case #3: i + left + right < target and right == len(arr) -1:
                # left += 1
                #right = len(arr) -1
        #case #4: i + left + right > target:
                #right -= 1

        res = []
        nums.sort()

        for i in range(0, len(nums)):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) -1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                elif threeSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left -= 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
        return res
