class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #Understanding
        #Input: an array of ints, already sorted in non decreasing order
        #Output: index1 < index2, so the first index has to be less than the second index
                #return an array [index1, and index2]

        # = index:  [1,2,3, 4]
        #numbers = [2,7,11,15], target = 9
        #return :[1,2]

        #target - current value = 
        # 9 - 2 = 7
        #Put 2 and it's index in the hashmap

        #hashMap = {} #number:index 
        #loop i in range (0, len(numbers)):
            # number_needed = target - numbers[i]
            # check to see if it's in the hashMap:
                # if it is, ensure the index < current_index
                    # return [index, current_index + 1]
                # if it isn't, add it to the hashMap
                #increment the index when added
        
        # [2,3,4], target = 6
        # i = 0, 6-2 = 4
        # hashMap = {i+1, 2}
        # i = 1, 6-3 = 3
        #hashMap = {(i+1, 2), (i+1, 3)}
        # i = 2, 6-4 = 2
        # index < current_index + 1
            
        # hashMap = {}  #number:index
        # for i in range(0,len(numbers)):
        #     number_needed = target - numbers[i]

        #     if (number_needed in hashMap and hashMap[number_needed] < i + 1):
        #         return [hashMap[number_needed], i + 1]
        #     else:
        #         hashMap[numbers[i]] = i + 1

        # return


        #Time complexity: O(n)


        # left = 0
        # right = 1

        # while left < right:

        #     if numbers[left] + numbers[right] == target:
        #         return [left+1, right+1]
        #     elif numbers[left] + numbers[right] < target and right < len(numbers) - 1:
        #         right += 1
        #     else:
        #         left += 1 
        #         right = left + 1
   
    
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
