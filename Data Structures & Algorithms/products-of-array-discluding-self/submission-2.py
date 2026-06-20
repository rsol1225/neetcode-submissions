class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Pseudocode:
            #index = [0,1,2,3] //for my knowledge
            #nums = [1,2,4,6]//nums[i]

            #calculate the product
            #product = 1;
            #for n in nums:
                #product *= n
           
            #result
            #for n in nums:
                #new_product = product/n
                #result.append(new_product)


            #return result

        #count the number of zeros
        #calculate the product
        count_zeros = 0;
        product = 1;
        for i in range(0, len(nums)):
            if nums[i] == 0:
                count_zeros += 1;
            else:
                product *= nums[i]

        
        result = []
        for n in nums:
            if n == 0 and count_zeros > 1:
                result.append(0)
            elif n == 0 and count_zeros == 1:
                result.append(product)
            elif n != 0 and count_zeros >= 1:
                result.append(0)
            else:
                result.append(product//n)
        return result


