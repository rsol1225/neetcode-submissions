class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #non-decreasing order

        #[1,2,3,4]
        #[3,6,7,8]

        #add up to a given target number 
        #index1 < index2

        #use a pointer solution
        left = 0
        right = len(numbers) - 1

        #[1,2,3,4], target = 3

        #left = 0, right = 3
        #4+1 = 5, so b/c 5 is greater, we decrease right pointer
        #3+1 = 4, so b/c 4 is greater, we decrease right pointer
        #2+1 = 3, return 1 and 2

        #ensures that they won't be pointing at the same index
        result = []
        while right > left:
            rightNum = numbers[right]
            leftNum = numbers[left]
            total = rightNum + leftNum

            if total > target:
                right -= 1
            elif total < target:
                left += 1
            elif total == target:
                if rightNum != leftNum:
                    result.append(left+1)
                    result.append(right+1)
                    return result
        
        return []
            